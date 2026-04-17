"""Aplicador de regras de pagamento (juros/descontos) com configuração injetável."""

from dataclasses import dataclass

from Domain.Enums.PaymentType import PaymentType


@dataclass(frozen=True)
class PaymentConfig:
    """Configuração das regras de pagamento (juros/benefícios por forma)."""
    card_interest_up_to_limit: float = 0.02
    card_interest_over_limit: float = 0.05
    card_installments_limit: int = 6
    boleto_discount: float = 5.0
    pix_discount: float = 10.0


class PaymentRulesApplier:
    """Aplica regras de pagamento para calcular juros e ajustar desconto."""
    def __init__(self, config: PaymentConfig):
        """Inicializa o aplicador de regras.

        Args:
            config: Configuração das regras de juros/descontos.
        """
        self._config = config

    def apply(
        self,
        *,
        subtotal: float,
        current_discount: float,
        payment_type: PaymentType,
        installments: int,
    ) -> tuple[float, float]:
        """Aplica regras conforme a forma de pagamento.

        Args:
            subtotal: Subtotal do pedido.
            current_discount: Desconto acumulado até o momento.
            payment_type: Forma de pagamento selecionada.
            installments: Número de parcelas (quando aplicável).

        Returns:
            Tupla (juros_calculados, desconto_atualizado).
        """
        interest = 0.0
        discount = current_discount

        if payment_type == PaymentType.CARD:
            if installments > 1 and installments <= self._config.card_installments_limit:
                interest = subtotal * self._config.card_interest_up_to_limit
            elif installments > self._config.card_installments_limit:
                interest = subtotal * self._config.card_interest_over_limit
            return interest, discount

        if payment_type == PaymentType.BOLETO:
            return interest, discount + self._config.boleto_discount

        if payment_type == PaymentType.PIX:
            return interest, discount + self._config.pix_discount

        if payment_type == PaymentType.CASH:
            return interest, discount

        raise ValueError("Forma de pagamento inválida")
