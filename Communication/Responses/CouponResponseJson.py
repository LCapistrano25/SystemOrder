from dataclasses import dataclass


@dataclass
class CouponResponseJson:
    id: int
    code: str
    discount: float

    @classmethod
    def from_payload(cls, payload: dict) -> "CouponResponseJson":
        return cls(id=payload["id"], code=payload["code"], discount=payload["discount"])

    def to_dict(self) -> dict:
        return {"id": self.id, "code": self.code, "discount": self.discount}
