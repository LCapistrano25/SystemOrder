from dataclasses import dataclass
from Communication.Responses.AddressResponseJson import AddressResponse



@dataclass
class FreightResponseJson:
    id: int
    address: AddressResponse
    total_weight: float
    price: float
    express_delivery: bool

    @classmethod
    def from_payload(cls, payload: dict) -> "FreightResponseJson":
        return cls(
            id=payload["id"],
            address=AddressResponse.from_payload(payload["address"]),
            total_weight=payload["total_weight"],
            price=payload["price"],
            express_delivery=payload["express_delivery"],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "address": self.address.to_dict(),
            "total_weight": self.total_weight,
            "price": self.price,
            "express_delivery": self.express_delivery,
        }
