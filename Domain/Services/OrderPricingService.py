"""Serviço de domínio que orquestra o cálculo de preços (subtotal, descontos, frete, juros e total)."""

from Domain.Entities.Order import Order
from Domain.Enums.CustomerType import CustomerType
from Domain.Services.OrderPricing.coupons.coupon_applier import CouponApplier
from Domain.Services.OrderPricing.freight.freight_calculator import FreightCalculator
from Domain.Services.OrderPricing.item.order_subtotal_calculator import OrderSubtotalCalculator
from Domain.Services.OrderPricing.order.order_pricing_result import OrderPricingResult
from Domain.Services.OrderPricing.payment.customer_discount_calculator import CustomerDiscountCalculator
from Domain.Services.OrderPricing.payment.payment_rules_applier import PaymentRulesApplier


class OrderPricingService:
    def __init__(
        self,
        *,
        subtotal_calculator: OrderSubtotalCalculator,
        customer_discount_calculator: CustomerDiscountCalculator,
        coupon_applier: CouponApplier,
        freight_calculator: FreightCalculator,
        payment_rules_applier: PaymentRulesApplier,
    ):
        self._subtotal_calculator = subtotal_calculator
        self._customer_discount_calculator = customer_discount_calculator
        self._coupon_applier = coupon_applier
        self._freight_calculator = freight_calculator
        self._payment_rules_applier = payment_rules_applier

    def calculate(self, order: Order) -> OrderPricingResult:
        subtotal = self._subtotal_calculator.calculate(order)
        customer_type = order.customer.customer_type
        discount = self._customer_discount_calculator.calculate(subtotal, customer_type)
        freight = self._freight_calculator.calculate(
            country=order.freight.address.country,
            total_weight=order.freight.total_weight,
            express_delivery=order.freight.express_delivery,
        )

        messages: list[str] = []
        discount, freight = self._apply_coupon_if_present(
            order=order,
            subtotal=subtotal,
            current_discount=discount,
            current_freight=freight,
            customer_type=customer_type,
            messages=messages,
        )

        interest, discount = self._payment_rules_applier.apply(
            subtotal=subtotal,
            current_discount=discount,
            payment_type=order.payment.payment_type,
            installments=order.payment.installments,
        )

        total = subtotal - discount + freight + interest
        if total < 0:
            total = 0

        return OrderPricingResult(
            subtotal=subtotal,
            discount=discount,
            freight=freight,
            interest=interest,
            total=total,
            messages=messages,
        )

    def _apply_coupon_if_present(
        self,
        *,
        order: Order,
        subtotal: float,
        current_discount: float,
        current_freight: float,
        customer_type: CustomerType,
        messages: list[str],
    ) -> tuple[float, float]:
        if order.coupon is None:
            return current_discount, current_freight

        coupon_messages, discount, freight = self._coupon_applier.apply(
            subtotal=subtotal,
            current_discount=current_discount,
            current_freight=current_freight,
            coupon_code=order.coupon.code,
            customer_type=customer_type,
        )
        messages.extend(coupon_messages)
        return discount, freight
