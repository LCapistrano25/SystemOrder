from Domain.Entities.Coupon import Coupon
from Domain.Entities.Customer import Customer
from Domain.Entities.Item import Item
from Domain.Entities.Payment import Payment
from Domain.Entities.Freight import Freight
from Domain.Entities.base.EntityBase import EntityBase
from Domain.ValuesObjects.Address import Address

class Order(EntityBase):
    def __init__(
        self,
        id: int,
        customer: Customer,
        items: list[Item],
        payment: Payment,
        freight: Freight,
        coupon: Coupon = None,
    ):
        super().__init__(id)
        self.customer = customer
        self.items = items
        self.freight = freight
        self.payment = payment
        self.coupon = coupon
        self._validate()

    def _validate(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Order ID must be a positive integer")
        
        if not isinstance(self.customer, Customer):
            raise ValueError("Invalid customer")
        
        if self.customer.blocked:
            raise ValueError("Blocked customers cannot place orders")
        
        if not self.items or len(self.items) == 0:
            raise ValueError("Order must have at least one item")
        
        if not all(isinstance(item, Item) for item in self.items):
            raise ValueError("All items must be valid Item instances")
        
        if not isinstance(self.freight.address, Address):
            raise ValueError("Invalid address")
        
        if self.freight.total_weight <= 0:
            raise ValueError("Total weight must be greater than zero")
        
        if not isinstance(self.payment, Payment):
            raise ValueError("Invalid payment method")
        
        if self.coupon is not None and not isinstance(self.coupon, Coupon):
            raise ValueError("Invalid coupon")

    def __str__(self):
        coupon_code = self.coupon.code if self.coupon is not None else None
        return (
            f"Order(ID: {self.id}, "
            f"Customer(ID: {self.customer.id}, Name: {self.customer.name}, Email: {self.customer.email}, Blocked: {self.customer.blocked}), "
            f"Items: {len(self.items)}, "
            f"Address: {self.freight.address}, "
            f"Total Weight: {self.freight.total_weight}, "
            f"Payment(ID: {self.payment.id}, Type: {self.payment.payment_type.name}, Installments: {self.payment.installments}), "
            f"Coupon: {coupon_code}, "
            f"Express Delivery: {self.freight.express_delivery})"
        )
