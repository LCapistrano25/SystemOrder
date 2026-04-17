"""Factory do grafo padrão de dependências do OrderPricingService (composition root)."""

from Domain.Services.OrderPricing.coupons import build_default_coupon_applier
from Domain.Services.OrderPricing.freight.config import FreightConfig
from Domain.Services.OrderPricing.freight.freight_calculator import FreightCalculator
from Domain.Services.OrderPricing.item.order_subtotal_calculator import OrderSubtotalCalculator
from Domain.Services.OrderPricing.order.order_pricing_service import OrderPricingService
from Domain.Services.OrderPricing.payment.customer_discount_calculator import CustomerDiscountCalculator
from Domain.Services.OrderPricing.payment.payment_rules_applier import PaymentConfig, PaymentRulesApplier


def build_order_pricing_service() -> OrderPricingService:
    """Constrói o serviço padrão de precificação com configurações default."""
    return OrderPricingService(
        subtotal_calculator=OrderSubtotalCalculator(),
        customer_discount_calculator=CustomerDiscountCalculator(),
        coupon_applier=build_default_coupon_applier(),
        freight_calculator=_build_freight_calculator(),
        payment_rules_applier=_build_payment_rules_applier(),
    )

def _build_freight_calculator() -> FreightCalculator:
    """Monta a calculadora de frete com configuração padrão."""
    return FreightCalculator(FreightConfig())

def _build_payment_rules_applier() -> PaymentRulesApplier:
    """Monta o aplicador de regras de pagamento com configuração padrão."""
    return PaymentRulesApplier(PaymentConfig())

