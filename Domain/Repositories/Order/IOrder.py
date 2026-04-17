from abc import ABC, abstractmethod
from Domain.Entities.Order import Order


class IOrder(ABC):
    @abstractmethod
    def get_order(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def add_order(self, order: Order) -> None:
        pass

    @abstractmethod
    def update_order(self, order: Order) -> None:
        pass

    @abstractmethod
    def delete_order(self, order_id: int) -> None:
        pass
