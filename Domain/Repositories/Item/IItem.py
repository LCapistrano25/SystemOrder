from abc import ABC, abstractmethod
from Domain.Entities.Item import Item


class IItem(ABC):
    @abstractmethod
    def get_item(self, item_id: int) -> Item:
        pass

    @abstractmethod
    def add_item(self, item: Item) -> None:
        pass

    @abstractmethod
    def update_item(self, item: Item) -> None:
        pass

    @abstractmethod
    def delete_item(self, item_id: int) -> None:
        pass
