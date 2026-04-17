from Domain.ValuesObjects.Email import Email
from Domain.Enums.CustomerType import CustomerType
from Domain.Entities.base.EntityBase import EntityBase

class Customer(EntityBase):
    """Entidade de Cliente"""
    def __init__(
        self,
        name: str,
        email: str,
        customer_type: CustomerType,
        id: int | None = None,
    ):
        """Inicializa um cliente e valida seus invariantes.

        Args:
            name: Nome do cliente.
            email: E-mail em formato texto (será convertido para Value Object).
            customer_type: Tipo do cliente.
            id: Identificador do cliente (opcional, normalmente definido pela persistência).
        """
        super().__init__(id)
        self.name = name
        self.email = Email.create(email)
        self.customer_type = customer_type
        self.blocked = False
        self._validate()

    def _validate(self):
        """Regras de validação de cliente."""
        if not self.name or len(self.name) < 2:
            raise ValueError("Name must have at least 2 characters")
        if not isinstance(self.customer_type, CustomerType):
            raise ValueError("Invalid customer type")

    def block(self):
        """Bloquear cliente."""
        if self.blocked:
            raise ValueError("Customer is already blocked")
        self.blocked = True

    def unblock(self):
        """Desbloquear cliente."""
        if not self.blocked:
            raise ValueError("Customer is not blocked")
        self.blocked = False

    def __str__(self):
        """Representação textual do cliente, útil para logs e depuração."""
        return f"Customer(Name: {self.name}, Email: {self.email}, Type: {self.customer_type.name}, Blocked: {self.blocked})"
