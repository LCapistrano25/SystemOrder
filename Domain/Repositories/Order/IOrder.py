from abc import ABC, abstractmethod
from Domain.Entities.Order import Order


class IOrder(ABC):
    """Contrato de repositório de pedidos."""
    @abstractmethod
    def get_order(self, order_id: int) -> Order:
        """Obtém um pedido pelo identificador.

        Args:
            order_id: Identificador do pedido.

        Returns:
            Pedido encontrado.
        """
        raise NotImplementedError

    @abstractmethod
    def add_order(self, order: Order) -> None:
        """Persiste um novo pedido.

        Args:
            order: Pedido a ser adicionado.
        """
        raise NotImplementedError

    @abstractmethod
    def update_order(self, order: Order) -> None:
        """Atualiza um pedido existente.

        Args:
            order: Pedido com dados atualizados.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_order(self, order_id: int) -> None:
        """Remove um pedido pelo identificador.

        Args:
            order_id: Identificador do pedido.
        """
        raise NotImplementedError
