from datetime import datetime

from Application.UseCases.Order.ProcessOrder.IProcessOrder import IProcessOrder
from Application.UseCases.Order.ProcessOrder.ProcessOrderInput import ProcessOrderInput
from Application.UseCases.Order.ProcessOrder.ProcessOrderOutput import ProcessOrderOutput
from Domain.Repositories.Order.IOrder import IOrder
from Domain.Services.OrderAlertService import OrderAlertService
from Domain.Services.OrderPricingService import OrderPricingService


class ProcessOrderUseCase(IProcessOrder):
    def __init__(
        self,
        order_repository: IOrder,
        pricing_service: OrderPricingService | None = None,
        alert_service: OrderAlertService | None = None,
    ):
        self._order_repository = order_repository
        self._pricing_service = pricing_service or OrderPricingService()
        self._alert_service = alert_service or OrderAlertService()
        self._logs: list[str] = []

    def execute(self, input_data: ProcessOrderInput) -> ProcessOrderOutput:
        if input_data.order_id <= 0:
            raise ValueError("Pedido inválido")

        order = self._order_repository.get_order(input_data.order_id)

        pricing = self._pricing_service.calculate(order)
        messages = list(pricing.messages)
        messages.extend(
            self._alert_service.get_alerts(
                subtotal=pricing.subtotal,
                customer_type=order.customer.customer_type,
                payment_type=order.payment.payment_type,
                country=order.freight.address.country,
            )
        )

        if input_data.send_email:
            messages.append(f"Email enviado para {order.customer.email.value}")

        logs: list[str] = []
        if input_data.save_log:
            logs = [
                f"Pedido: {order.id}",
                f"Cliente: {order.customer.name}",
                f"Subtotal: {pricing.subtotal}",
                f"Desconto: {pricing.discount}",
                f"Frete: {pricing.freight}",
                f"Juros: {pricing.interest}",
                f"Total: {pricing.total}",
                f"Data: {datetime.now()}",
            ]
            self._logs.extend(logs)

        result_text = ""
        for message in messages:
            result_text += f"{message}\n"
        result_text += f"TOTAL_FINAL={pricing.total}\n"

        return ProcessOrderOutput(
            order_id=order.id,
            subtotal=pricing.subtotal,
            discount=pricing.discount,
            freight=pricing.freight,
            interest=pricing.interest,
            total=pricing.total,
            messages=messages,
            logs=logs,
            result_text=result_text,
        )

    def get_logs(self) -> list[str]:
        return list(self._logs)
