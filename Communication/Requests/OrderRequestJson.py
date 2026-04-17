from dataclasses import dataclass


@dataclass
class OrderRequest:
    id: int
    customer_id: int
    item_ids: list[int]
    payment_id: int
    freight_id: int
    coupon_id: int | None

    @classmethod
    def from_body(cls, body: dict, entity_id: int | None = None) -> "OrderRequest":
        coupon_id = body.get("coupon_id")
        return cls(
            id=entity_id if entity_id is not None else int(body["id"]),
            customer_id=int(body["customer_id"]),
            item_ids=[int(item_id) for item_id in body["item_ids"]],
            payment_id=int(body["payment_id"]),
            freight_id=int(body["freight_id"]),
            coupon_id=int(coupon_id) if coupon_id is not None else None,
        )

    def to_payload(self) -> dict:
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "item_ids": self.item_ids,
            "payment_id": self.payment_id,
            "freight_id": self.freight_id,
            "coupon_id": self.coupon_id,
        }
