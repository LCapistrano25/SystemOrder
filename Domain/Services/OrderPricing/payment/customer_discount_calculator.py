"""Calculadora de desconto por tipo de cliente (fail-fast para tipos desconhecidos)."""

from Domain.Enums.CustomerType import CustomerType


class CustomerDiscountCalculator:
    """Calcula desconto percentual com base no tipo do cliente."""
    def __init__(self, rates: dict[CustomerType, float] | None = None):
        """Inicializa a calculadora de descontos por tipo de cliente.

        Args:
            rates: Mapeamento opcional CustomerType -> taxa de desconto.
        """
        self._rates = rates or {
            CustomerType.VIP: 0.15,
            CustomerType.PREMIUM: 0.10,
            CustomerType.STANDARD: 0.02,
            CustomerType.NEW: 0.0,
        }

    def calculate(self, subtotal: float, customer_type: CustomerType) -> float:
        """Calcula o desconto a partir do subtotal e do tipo do cliente.

        Raises:
            ValueError: Quando o tipo do cliente não estiver configurado.
        """
        try:
            rate = self._rates[customer_type]
        except KeyError as exc:
            raise ValueError(f"Tipo de cliente desconhecido: {customer_type}") from exc
        return subtotal * rate
