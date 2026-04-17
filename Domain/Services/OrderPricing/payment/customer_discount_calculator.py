"""Calculadora de desconto por tipo de cliente (fail-fast para tipos desconhecidos)."""

from Domain.Enums.CustomerType import CustomerType


class CustomerDiscountCalculator:
    def __init__(self, rates: dict[CustomerType, float] | None = None):
        self._rates = rates or {
            CustomerType.VIP: 0.15,
            CustomerType.PREMIUM: 0.10,
            CustomerType.STANDARD: 0.02,
            CustomerType.NEW: 0.0,
        }

    def calculate(self, subtotal: float, customer_type: CustomerType) -> float:
        try:
            rate = self._rates[customer_type]
        except KeyError as exc:
            raise ValueError(f"Tipo de cliente desconhecido: {customer_type}") from exc
        return subtotal * rate
