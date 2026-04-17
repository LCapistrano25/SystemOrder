from Domain.ValuesObjects.Address import Address
from Domain.Entities.base.EntityBase import EntityBase

class Freight(EntityBase):
    def __init__(self, id: int, address: Address, total_weight: float, price: float, express_delivery: bool = False):
        super().__init__(id)
        self.address = address
        self.total_weight = total_weight
        self.price = price
        self.express_delivery = express_delivery
        self._validate()

    def _validate(self):
        if not isinstance(self.address, Address):
            raise ValueError("Invalid address")
        if self.total_weight <= 0:
            raise ValueError("Weight must be greater than zero")
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if not isinstance(self.express_delivery, bool):
            raise ValueError("Express delivery must be a boolean value")

    def __str__(self):
        return f"Freight(ID: {self.id}, Address: {self.address}, Total Weight: {self.total_weight}, Price: {self.price}, Express Delivery: {self.express_delivery})"
