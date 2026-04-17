from dataclasses import dataclass

from Communication.Enums.PaymentTypeJson import PaymentTypeJson


@dataclass
class PaymentRequest:
    id: int
    payment_type: int
    installments: int

    @classmethod
    def from_body(cls, body: dict, entity_id: int | None = None) -> "PaymentRequest":
        return cls(
            id=entity_id if entity_id is not None else int(body["id"]),
            payment_type=PaymentTypeJson.from_json(body["payment_type"]).value,
            installments=int(body["installments"]),
        )

    def to_payload(self) -> dict:
        return {
            "id": self.id,
            "payment_type": self.payment_type,
            "installments": self.installments,
        }
