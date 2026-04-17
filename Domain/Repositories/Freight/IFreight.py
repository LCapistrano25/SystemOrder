from abc import ABC, abstractmethod
from Domain.Entities.Freight import Freight


class IFreight(ABC):
    @abstractmethod
    def get_freight(self, freight_id: int) -> Freight:
        pass

    @abstractmethod
    def add_freight(self, freight: Freight) -> None:
        pass

    @abstractmethod
    def update_freight(self, freight: Freight) -> None:
        pass

    @abstractmethod
    def delete_freight(self, freight_id: int) -> None:
        pass
