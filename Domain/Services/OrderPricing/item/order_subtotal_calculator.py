"""Calculadora do subtotal de um pedido com ajustes por categoria de item."""

from Domain.Entities.Order import Order
from Domain.Enums.Category import Category


class OrderSubtotalCalculator:
    def __init__(self, food_surcharge: float = 2.0, imported_surcharge: float = 5.0):
        self._food_surcharge = food_surcharge
        self._imported_surcharge = imported_surcharge

    def calculate(self, order: Order) -> float:
        subtotal = 0.0
        for item in order.items:
            subtotal += item.price * item.quantity
            if item.category == Category.FOOD:
                subtotal += self._food_surcharge
            elif item.category == Category.IMPORTED:
                subtotal += self._imported_surcharge
        return subtotal

