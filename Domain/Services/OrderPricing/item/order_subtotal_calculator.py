"""Calculadora do subtotal de um pedido com ajustes por categoria de item."""

from Domain.Entities.Order import Order
from Domain.Enums.Category import Category


class OrderSubtotalCalculator:
    """Calcula o subtotal do pedido, incluindo ajustes por categoria."""
    def __init__(self, food_surcharge: float = 2.0, imported_surcharge: float = 5.0):
        """Inicializa a calculadora de subtotal.

        Args:
            food_surcharge: Adicional para itens da categoria FOOD.
            imported_surcharge: Adicional para itens da categoria IMPORTED.
        """
        self._food_surcharge = food_surcharge
        self._imported_surcharge = imported_surcharge

    def calculate(self, order: Order) -> float:
        """Calcula o subtotal somando itens e eventuais adicionais por categoria."""
        subtotal = 0.0
        for item in order.items:
            subtotal += item.price * item.quantity
            if item.category == Category.FOOD:
                subtotal += self._food_surcharge
            elif item.category == Category.IMPORTED:
                subtotal += self._imported_surcharge
        return subtotal
