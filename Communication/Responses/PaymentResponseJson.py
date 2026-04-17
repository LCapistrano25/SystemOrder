from dataclasses import dataclass


@dataclass
class PaymentResponseJson:
    id: int
    payment_type: str
    installments: int

    @classmethod
    def from_payload(cls, payload: dict) -> "PaymentResponseJson":
        return cls(
            id=payload["id"],
            payment_type=payload["payment_type"],
            installments=payload["installments"],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "payment_type": self.payment_type,
            "installments": self.installments,
        }
