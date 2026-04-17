from abc import ABC, abstractmethod
from Domain.Entities.Item import Item


class IItem(ABC):
    """Contrato de repositório de itens."""
    @abstractmethod
    def get_item(self, item_id: int) -> Item:
        """Obtém um item pelo identificador.

        Args:
            item_id: Identificador do item.

        Returns:
            Item encontrado.
        """
        raise NotImplementedError

    @abstractmethod
    def add_item(self, item: Item) -> None:
        """Persiste um novo item.

        Args:
            item: Item a ser adicionado.
        """
        raise NotImplementedError

    @abstractmethod
    def update_item(self, item: Item) -> None:
        """Atualiza um item existente.

        Args:
            item: Item com dados atualizados.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_item(self, item_id: int) -> None:
        """Remove um item pelo identificador.

        Args:
            item_id: Identificador do item.
        """
        raise NotImplementedError
