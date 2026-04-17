from dataclasses import dataclass

from Communication.Responses.CouponResponseJson import CouponResponseJson
from Communication.Responses.CustomerResponseJson import CustomerResponseJson
from Communication.Responses.FreightResponseJson import FreightResponseJson
from Communication.Responses.ItemResponseJson import ItemResponseJson
from Communication.Responses.PaymentResponseJson import PaymentResponseJson



@dataclass
class OrderResponseJson:
    id: int
    customer: CustomerResponseJson
    items: list[ItemResponseJson]
    payment: PaymentResponseJson
    freight: FreightResponseJson
    coupon: CouponResponseJson | None

    @classmethod
    def from_payload(cls, payload: dict) -> "OrderResponseJson":
        coupon = payload["coupon"]
        return cls(
            id=payload["id"],
            customer=CustomerResponseJson.from_payload(payload["customer"]),
            items=[ItemResponseJson.from_payload(item) for item in payload["items"]],
            payment=PaymentResponseJson.from_payload(payload["payment"]),
            freight=FreightResponseJson.from_payload(payload["freight"]),
            coupon=CouponResponseJson.from_payload(coupon) if coupon is not None else None,
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "customer": self.customer.to_dict(),
            "items": [item.to_dict() for item in self.items],
            "payment": self.payment.to_dict(),
            "freight": self.freight.to_dict(),
            "coupon": self.coupon.to_dict() if self.coupon is not None else None,
        }
