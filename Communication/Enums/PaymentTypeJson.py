from enum import IntEnum

class PaymentTypeJson(IntEnum):
    CARD = 1
    CASH = 2
    PIX = 3
    BOLETO = 4

    @staticmethod
    def to_json(value: "PaymentTypeJson") -> str:
        return value.name

    @staticmethod
    def from_json(value: str | int) -> "PaymentTypeJson":
        if isinstance(value, int):
            return PaymentTypeJson(value)
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Invalid payment_type")
        return PaymentTypeJson[value.strip().upper()]
