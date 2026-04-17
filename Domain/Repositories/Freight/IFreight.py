from abc import ABC, abstractmethod
from Domain.Entities.Freight import Freight


class IFreight(ABC):
    """Contrato de repositório de fretes."""
    @abstractmethod
    def get_freight(self, freight_id: int) -> Freight:
        """Obtém um frete pelo identificador.

        Args:
            freight_id: Identificador do frete.

        Returns:
            Frete encontrado.
        """
        raise NotImplementedError

    @abstractmethod
    def add_freight(self, freight: Freight) -> None:
        """Persiste um novo frete.

        Args:
            freight: Frete a ser adicionado.
        """
        raise NotImplementedError

    @abstractmethod
    def update_freight(self, freight: Freight) -> None:
        """Atualiza um frete existente.

        Args:
            freight: Frete com dados atualizados.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_freight(self, freight_id: int) -> None:
        """Remove um frete pelo identificador.

        Args:
            freight_id: Identificador do frete.
        """
        raise NotImplementedError
