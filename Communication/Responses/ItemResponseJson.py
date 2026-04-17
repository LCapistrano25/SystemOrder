from dataclasses import dataclass


@dataclass
class ItemResponseJson:
    id: int
    name: str
    price: float
    quantity: int
    category: str

    @classmethod
    def from_payload(cls, payload: dict) -> "ItemResponseJson":
        return cls(
            id=payload["id"],
            name=payload["name"],
            price=payload["price"],
            quantity=payload["quantity"],
            category=payload["category"],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
        }
