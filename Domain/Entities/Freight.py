from Domain.ValuesObjects.Address import Address
from Domain.Entities.base.EntityBase import EntityBase

class Freight(EntityBase):
    """Entidade de Frete, com endereço, peso e preço."""
    def __init__(self, id: int, address: Address, total_weight: float, price: float, express_delivery: bool = False):
        """Inicializa um frete e valida seus invariantes.

        Args:
            id: Identificador do frete.
            address: Endereço de entrega.
            total_weight: Peso total da entrega (maior que zero).
            price: Valor do frete (não negativo).
            express_delivery: Indica entrega expressa.
        """
        super().__init__(id)
        self.address = address
        self.total_weight = total_weight
        self.price = price
        self.express_delivery = express_delivery
        self._validate()

    def _validate(self):
        """Regras de validação do frete."""
        if not isinstance(self.address, Address):
            raise ValueError("Invalid address")
        if self.total_weight <= 0:
            raise ValueError("Weight must be greater than zero")
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if not isinstance(self.express_delivery, bool):
            raise ValueError("Express delivery must be a boolean value")

    def __str__(self):
        """Representação textual do frete, útil para logs e depuração."""
        return f"Freight(ID: {self.id}, Address: {self.address}, Total Weight: {self.total_weight}, Price: {self.price}, Express Delivery: {self.express_delivery})"
