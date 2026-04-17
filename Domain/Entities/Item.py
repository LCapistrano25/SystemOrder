from Domain.Enums.Category import Category
from Domain.Entities.base.EntityBase import EntityBase

class Item(EntityBase):
    def __init__(self, id: int, name: str, price: float, quantity: int, category: Category):
        super().__init__(id)
        self.name = name.strip() if name else name
        self.price = price
        self.quantity = quantity
        self.category = category
        self._validate()

    def _validate(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        
        if not isinstance(self.category, Category):
            raise ValueError("Invalid category")

    def __str__(self):
        return f"Item(ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Category: {self.category.name})"
