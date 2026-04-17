"""DTO de saída do cálculo de precificação de um pedido."""

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderPricingResult:
    subtotal: float
    discount: float
    freight: float
    interest: float
    total: float
    messages: list[str]

