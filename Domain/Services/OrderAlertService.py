from Domain.Enums.CustomerType import CustomerType
from Domain.Enums.PaymentType import PaymentType


class OrderAlertService:
    """Serviço de domínio para geração de alertas e recomendações de pedido."""
    def get_alerts(
        self,
        *,
        subtotal: float,
        customer_type: CustomerType,
        payment_type: PaymentType,
        country: str,
    ) -> list[str]:
        """Gera alertas/recomendações com base em regras de negócio do pedido.

        Args:
            subtotal: Subtotal do pedido.
            customer_type: Tipo do cliente.
            payment_type: Forma de pagamento.
            country: País do endereço de entrega.

        Returns:
            Lista de mensagens de alerta/recomendação.
        """
        messages: list[str] = []

        if subtotal > 1000:
            messages.append("Pedido de alto valor")

        if subtotal > 5000 and customer_type == CustomerType.NEW:
            messages.append("Pedido suspeito para cliente novo")

        if payment_type == PaymentType.BOLETO and subtotal > 3000:
            messages.append("Pedido com boleto acima do limite recomendado")

        if (country or "").strip().upper() != "BR" and subtotal < 100:
            messages.append("Pedido internacional abaixo do valor mínimo recomendado")

        return messages
