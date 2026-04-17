from Application.UseCases.Customer.CustomerOutput import CustomerOutput
from Domain.Repositories.Customer.ICustomer import ICustomer


class GetCustomersUseCase:
    """Caso de uso responsável por listar clientes."""
    def __init__(self, customer_repository: ICustomer):
        """Inicializa o caso de uso.

        Args:
            customer_repository: Repositório de clientes utilizado para leitura.
        """
        self._customer_repository = customer_repository

    def execute(self) -> list[CustomerOutput]:
        """Lista clientes e converte para DTO de saída.

        Returns:
            Lista de clientes no formato de saída da camada de aplicação.
        """
        customers = self._customer_repository.list_customers()
        return [
            CustomerOutput(
                id=customer.id,
                name=customer.name,
                email=customer.email.value,
                customer_type=customer.customer_type.name,
                blocked=customer.blocked,
            )
            for customer in customers
        ]
