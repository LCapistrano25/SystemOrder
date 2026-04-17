from Application.UseCases.Customer.CustomerInput import CustomerInput
from Application.UseCases.Customer.CustomerOutput import CustomerOutput
from Application.UseCases.Customer.CreateCustomer.CreateCustomerValidator import CreateCustomerValidator

from Application.UseCases.Customer.CreateCustomer.ICreateCustomer import ICreateCustomer
from Domain.Entities.Customer import Customer
from Domain.Enums.CustomerType import CustomerType
from Domain.Repositories.Customer.ICustomer import ICustomer


class CreateCustomerUseCase(ICreateCustomer):
    """Caso de uso responsável por criar um cliente e persistir no repositório."""
    def __init__(self, customer_repository: ICustomer, validator: CreateCustomerValidator | None = None):
        """Inicializa o caso de uso.

        Args:
            customer_repository: Repositório de clientes utilizado para persistência.
            validator: Validador do input. Se não informado, usa o validador padrão.
        """
        self._customer_repository = customer_repository
        self._validator = validator or CreateCustomerValidator()

    def execute(self, customer: CustomerInput) -> CustomerOutput:
        """Cria um cliente a partir do input, aplica regras e salva no repositório.

        Args:
            customer: Dados de entrada para criação do cliente.

        Returns:
            DTO de saída com os dados do cliente criado.
        """
        self._validator.validate(customer)  

        entity = Customer(
            name=customer.name,
            email=customer.email,
            customer_type=CustomerType(customer.customer_type),
        )
        if customer.blocked:
            entity.block()

        self._customer_repository.add_customer(entity)

        return CustomerOutput(
            id=entity.id,
            name=entity.name,
            email=entity.email.value,
            customer_type=entity.customer_type.name,
            blocked=entity.blocked,
        )
