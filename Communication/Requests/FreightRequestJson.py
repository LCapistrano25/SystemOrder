from dataclasses import dataclass


@dataclass
class FreightRequest:
    id: int
    street: str
    city: str
    state: str
    zip_code: str
    total_weight: float
    price: float
    express_delivery: bool

    @classmethod
    def from_body(cls, body: dict, entity_id: int | None = None) -> "FreightRequest":
        address = body["address"]
        return cls(
            id=entity_id if entity_id is not None else int(body["id"]),
            street=str(address["street"]),
            city=str(address["city"]),
            state=str(address["state"]),
            zip_code=str(address["zip_code"]),
            total_weight=float(body["total_weight"]),
            price=float(body["price"]),
            express_delivery=bool(body.get("express_delivery", False)),
        )

    def to_payload(self) -> dict:
        return {
            "id": self.id,
            "address": {
                "street": self.street,
                "city": self.city,
                "state": self.state,
                "zip_code": self.zip_code,
            },
            "total_weight": self.total_weight,
            "price": self.price,
            "express_delivery": self.express_delivery,
        }
