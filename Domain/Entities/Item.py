from Domain.Enums.Category import Category
from Domain.Entities.base.EntityBase import EntityBase

class Item(EntityBase):
    """Entidade de Item do pedido (produto/serviço com preço e quantidade)."""
    def __init__(self, id: int, name: str, price: float, quantity: int, category: Category):
        """Inicializa um item e valida seus invariantes.

        Args:
            id: Identificador do item.
            name: Nome do item.
            price: Preço unitário (não negativo).
            quantity: Quantidade (maior que zero).
            category: Categoria do item.
        """
        super().__init__(id)
        self.name = name.strip() if name else name
        self.price = price
        self.quantity = quantity
        self.category = category
        self._validate()

    def _validate(self):
        """Regras de validação do item."""
        if not self.name:
            raise ValueError("Name cannot be empty")
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        
        if not isinstance(self.category, Category):
            raise ValueError("Invalid category")

    def __str__(self):
        """Representação textual do item, útil para logs e depuração."""
        return f"Item(ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Category: {self.category.name})"
