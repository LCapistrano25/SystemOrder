from dataclasses import dataclass


@dataclass
class CouponRequest:
    id: int
    code: str
    discount: float

    @classmethod
    def from_body(cls, body: dict, entity_id: int | None = None) -> "CouponRequest":
        return cls(
            id=entity_id if entity_id is not None else int(body["id"]),
            code=str(body["code"]),
            discount=float(body["discount"]),
        )

    def to_payload(self) -> dict:
        return {"id": self.id, "code": self.code, "discount": self.discount}
