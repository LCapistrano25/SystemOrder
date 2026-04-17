"""Pacote de cupons: expõe o aplicador e as strategies disponíveis."""

from Domain.Services.OrderPricing.coupons.coupon_applier import CouponApplier
from Domain.Services.OrderPricing.coupons.default_coupon_applier import DefaultCouponConfig, build_default_coupon_applier
from Domain.Services.OrderPricing.coupons.coupon_strategies import (
    CouponStrategy,
    FreeFreightCoupon,
    PercentDiscountCoupon,
    VipFixedDiscountCoupon,
)

__all__ = [
    "CouponApplier",
    "DefaultCouponConfig",
    "build_default_coupon_applier",
    "CouponStrategy",
    "PercentDiscountCoupon",
    "FreeFreightCoupon",
    "VipFixedDiscountCoupon",
]

