"""Strategies de cupom (OCP): cada classe representa uma regra de aplicação de cupom."""

from abc import ABC, abstractmethod

from Domain.Enums.CustomerType import CustomerType


class CouponStrategy(ABC):
    @abstractmethod
    def is_applicable(self, code: str, customer_type: CustomerType) -> bool:
        raise NotImplementedError

    @abstractmethod
    def apply(self, subtotal: float, discount: float, freight: float) -> tuple[float, float]:
        raise NotImplementedError


class PercentDiscountCoupon(CouponStrategy):
    def __init__(self, code: str, rate: float):
        self._code = code.strip().upper()
        self._rate = rate

    def is_applicable(self, code: str, customer_type: CustomerType) -> bool:
        return code == self._code

    def apply(self, subtotal: float, discount: float, freight: float) -> tuple[float, float]:
        return discount + subtotal * self._rate, freight


class FreeFreightCoupon(CouponStrategy):
    def __init__(self, code: str = "FRETEGRATIS"):
        self._code = code.strip().upper()

    def is_applicable(self, code: str, customer_type: CustomerType) -> bool:
        return code == self._code

    def apply(self, subtotal: float, discount: float, freight: float) -> tuple[float, float]:
        return discount, 0.0


class VipFixedDiscountCoupon(CouponStrategy):
    def __init__(self, code: str, required_type: CustomerType, amount: float):
        self._code = code.strip().upper()
        self._required_type = required_type
        self._amount = amount

    def is_applicable(self, code: str, customer_type: CustomerType) -> bool:
        return code == self._code and customer_type == self._required_type

    def apply(self, subtotal: float, discount: float, freight: float) -> tuple[float, float]:
        return discount + self._amount, freight

