"""Aplicador de cupons: seleciona a primeira strategy aplicável e retorna mensagens/valores atualizados."""

from Domain.Enums.CustomerType import CustomerType
from Domain.Services.OrderPricing.coupons.coupon_strategies import CouponStrategy


class CouponApplier:
    """Seleciona e aplica a strategy de cupom adequada, caso exista."""
    def __init__(self, strategies: list[CouponStrategy]):
        """Inicializa o aplicador com as strategies disponíveis.

        Args:
            strategies: Lista de strategies de cupom, avaliadas em ordem.
        """
        self._strategies = strategies

    def apply(
        self,
        *,
        subtotal: float,
        current_discount: float,
        current_freight: float,
        coupon_code: str,
        customer_type: CustomerType,
    ) -> tuple[list[str], float, float]:
        """Aplica o cupom informando ajustando desconto/frete.

        Returns:
            Tupla (mensagens, desconto_atualizado, frete_atualizado).
        """
        code = coupon_code.strip().upper()
        for strategy in self._strategies:
            if strategy.is_applicable(code, customer_type):
                discount, freight = strategy.apply(subtotal, current_discount, current_freight)
                return [], discount, freight
        return ["Cupom inválido ou não aplicável"], current_discount, current_freight
