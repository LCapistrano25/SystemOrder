import re
from Domain.Entities.base.EntityBase import EntityBase
class Coupon(EntityBase):
    def __init__(self, id: int, code: str, discount: float):
        super().__init__(id)
        self.code = code.strip() if code else code
        self.discount = discount
        self._validate()

    def _validate(self):
        if not self.code or not re.match(r'^[A-Z0-9]+$', self.code):
            raise ValueError("Coupon code must contain only uppercase letters and numbers")
        
        if self.discount <= 0 or self.discount > 100:
            raise ValueError("Discount must be between 1 and 100")

    def __str__(self):
        return f"Coupon(ID: {self.id}, Code: {self.code}, Discount: {self.discount}%)"
