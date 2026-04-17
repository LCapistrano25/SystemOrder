from abc import ABC, abstractmethod
from Domain.Entities.Customer import Customer


class ICustomer(ABC):
    @abstractmethod
    def get_customer(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def list_customers(self) -> list[Customer]:
        pass

    @abstractmethod
    def add_customer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def update_customer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int) -> None:
        pass
