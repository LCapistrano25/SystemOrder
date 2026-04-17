"""Aplicador de regras de pagamento (juros/descontos) com configuração injetável."""

from dataclasses import dataclass

from Domain.Enums.PaymentType import PaymentType


@dataclass(frozen=True)
class PaymentConfig:
    card_interest_up_to_limit: float = 0.02
    card_interest_over_limit: float = 0.05
    card_installments_limit: int = 6
    boleto_discount: float = 5.0
    pix_discount: float = 10.0


class PaymentRulesApplier:
    def __init__(self, config: PaymentConfig):
        self._config = config

    def apply(
        self,
        *,
        subtotal: float,
        current_discount: float,
        payment_type: PaymentType,
        installments: int,
    ) -> tuple[float, float]:
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