from Application.UseCases.Customer.CustomerInput import CustomerInput
from Domain.Enums.CustomerType import CustomerType


class CreateCustomerValidator:
    """Validador do input do caso de uso de criação de cliente."""
    def validate(self, customer: CustomerInput) -> None:
        """Valida dados de criação de cliente.

        Args:
            customer: DTO de entrada com os dados do cliente.

        Raises:
            ValueError: Quando algum campo obrigatório estiver ausente/inválido.
        """
        if not isinstance(customer.name, str) or not customer.name.strip():
            raise ValueError("Customer name is required")

        if not isinstance(customer.email, str) or not customer.email.strip():
            raise ValueError("Customer email is required")

        if not isinstance(customer.blocked, bool):
            raise ValueError("Customer blocked must be a boolean")

        if not isinstance(customer.customer_type, int):
            raise ValueError("Customer type must be an integer")
        CustomerType(customer.customer_type)
