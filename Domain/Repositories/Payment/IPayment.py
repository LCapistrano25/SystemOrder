from abc import ABC, abstractmethod
from Domain.Entities.Payment import Payment


class IPayment(ABC):
    @abstractmethod
    def get_payment(self, payment_id: int) -> Payment:
        pass

    @abstractmethod
    def add_payment(self, payment: Payment) -> None:
        pass

    @abstractmethod
    def update_payment(self, payment: Payment) -> None:
        pass

    @abstractmethod
    def delete_payment(self, payment_id: int) -> None:
        pass
