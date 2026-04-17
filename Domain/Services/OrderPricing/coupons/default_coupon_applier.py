"""Factory do conjunto padrão de cupons aceitos no sistema legado."""

from dataclasses import dataclass

from Domain.Enums.CustomerType import CustomerType
from Domain.Services.OrderPricing.coupons.coupon_applier import CouponApplier
from Domain.Services.OrderPricing.coupons.coupon_strategies import (
    FreeFreightCoupon,
    PercentDiscountCoupon,
    VipFixedDiscountCoupon,
)


@dataclass(frozen=True)
class DefaultCouponConfig:
    """Configuração padrão para cupons suportados no sistema."""
    desc10_code: str = "DESC10"
    desc10_rate: float = 0.10
    desc20_code: str = "DESC20"
    desc20_rate: float = 0.20
    free_freight_code: str = "FRETEGRATIS"
    vip50_code: str = "VIP50"
    vip50_required_type: CustomerType = CustomerType.VIP
    vip50_amount: float = 50.0


def build_default_coupon_applier(config: DefaultCouponConfig | None = None) -> CouponApplier:
    """Constrói um CouponApplier com o conjunto padrão de strategies.

    Args:
        config: Configuração opcional dos códigos/valores.

    Returns:
        Aplicador de cupons pronto para uso no pricing.
    """
    config = config or DefaultCouponConfig()
    return CouponApplier(
        strategies=[
            PercentDiscountCoupon(config.desc10_code, config.desc10_rate),
            PercentDiscountCoupon(config.desc20_code, config.desc20_rate),
            FreeFreightCoupon(config.free_freight_code),
            VipFixedDiscountCoupon(config.vip50_code, config.vip50_required_type, config.vip50_amount),
        ]
    )
