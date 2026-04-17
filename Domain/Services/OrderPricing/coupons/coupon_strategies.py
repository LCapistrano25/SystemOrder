"""Strategies de cupom (OCP): cada classe representa uma regra de aplicação de cupom."""

from abc import ABC, abstractmethod

from Domain.Enums.CustomerType import CustomerType


class CouponStrategy(ABC):
    """Contrato para regras de cupom (strategy) aplicáveis ao pricing."""
    @abstractmethod
    def is_applicable(self, code: str, customer_type: CustomerType) -> bool:
        """Indica se a strategy pode ser aplicada para o código e tipo de cliente."""
        raise NotImplementedError

    @abstractmethod
    def apply(self, subtotal: float, discount: float, freight: float) -> tuple[float, float]:
        """Aplica a regra do cupom e retorna (desconto_atualizado, frete_atualizado)."""
        raise NotImplementedError


class PercentDiscountCoupon(CouponStrategy):
    """Cupom que aplica desconto percentual sobre o subtotal."""
    def __init__(self, code: str, rate: float):
        """Inicializa o cupom percentual.

        Args:
            code: Código do cupom.
            rate: Taxa percentual (ex.: 0.10 para 10%).
        """
        self._code = code.strip().upper()
        self._rate = rate

    def is_applicable(self, code: str, customer_type: CustomerType) -> bool:
        """Retorna True quando o código corresponde ao cupom configurado."""
        return code == self._code

    def apply(self, subtotal: float, discount: float, freight: float) -> tuple[float, float]:
        """Acumula desconto percentual sobre o subtotal."""
        return discount + subtotal * self._rate, freight


class FreeFreightCoupon(CouponStrategy):
    """Cupom que zera o valor do frete."""
    def __init__(self, code: str = "FRETEGRATIS"):
        """Inicializa o cupom de frete grátis.

        Args:
            code: Código do cupom.
        """
        self._code = code.strip().upper()

    def is_applicable(self, code: str, customer_type: CustomerType) -> bool:
        """Retorna True quando o código corresponde ao cupom configurado."""
        return code == self._code

    def apply(self, subtotal: float, discount: float, freight: float) -> tuple[float, float]:
        """Zera o frete mantendo desconto inalterado."""
        return discount, 0.0


class VipFixedDiscountCoupon(CouponStrategy):
    """Cupom com desconto fixo aplicável apenas para um tipo de cliente específico."""
    def __init__(self, code: str, required_type: CustomerType, amount: float):
        """Inicializa o cupom de desconto fixo.

        Args:
            code: Código do cupom.
            required_type: Tipo de cliente exigido para aplicar.
            amount: Valor fixo a somar ao desconto.
        """
        self._code = code.strip().upper()
        self._required_type = required_type
        self._amount = amount

    def is_applicable(self, code: str, customer_type: CustomerType) -> bool:
        """Retorna True quando código e tipo do cliente atendem à regra."""
        return code == self._code and customer_type == self._required_type

    def apply(self, subtotal: float, discount: float, freight: float) -> tuple[float, float]:
        """Acumula desconto fixo mantendo o frete inalterado."""
        return discount + self._amount, freight
