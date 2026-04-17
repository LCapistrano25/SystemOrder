from dataclasses import dataclass

from Communication.Enums.CategoryJson import CategoryJson


@dataclass
class ItemRequest:
    id: int
    name: str
    price: float
    quantity: int
    category: int

    @classmethod
    def from_body(cls, body: dict, entity_id: int | None = None) -> "ItemRequest":
        return cls(
            id=entity_id if entity_id is not None else int(body["id"]),
            name=str(body["name"]),
            price=float(body["price"]),
            quantity=int(body["quantity"]),
            category=CategoryJson.from_json(body["category"]).value,
        )

    def to_payload(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
        }
