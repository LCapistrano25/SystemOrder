from Application.UseCases.Customer.CustomerOutput import CustomerOutput
from Domain.Repositories.Customer.ICustomer import ICustomer


class GetCustomersUseCase:
    def __init__(self, customer_repository: ICustomer):
        self._customer_repository = customer_repository

    def execute(self) -> list[CustomerOutput]:
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
