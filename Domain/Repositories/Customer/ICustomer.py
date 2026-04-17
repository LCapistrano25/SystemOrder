from abc import ABC, abstractmethod
from Domain.Entities.Customer import Customer


class ICustomer(ABC):
    """Contrato de repositório de clientes (persistência/leitura)."""
    @abstractmethod
    def get_customer(self, customer_id: int) -> Customer:
        """Obtém um cliente pelo identificador.

        Args:
            customer_id: Identificador do cliente.

        Returns:
            Cliente encontrado.
        """
        raise NotImplementedError

    @abstractmethod
    def list_customers(self) -> list[Customer]:
        """Lista todos os clientes.

        Returns:
            Lista de clientes.
        """
        raise NotImplementedError

    @abstractmethod
    def add_customer(self, customer: Customer) -> None:
        """Persiste um novo cliente.

        Args:
            customer: Cliente a ser adicionado.
        """
        raise NotImplementedError

    @abstractmethod
    def update_customer(self, customer: Customer) -> None:
        """Atualiza um cliente existente.

        Args:
            customer: Cliente com dados atualizados.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_customer(self, customer_id: int) -> None:
        """Remove um cliente pelo identificador.

        Args:
            customer_id: Identificador do cliente.
        """
        raise NotImplementedError
