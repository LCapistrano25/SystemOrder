from enum import Enum

class PaymentType(Enum):
    """Enum com formas de pagamento suportadas pelo domínio."""
    CARD = 1
    CASH = 2
    PIX = 3
    BOLETO = 4
