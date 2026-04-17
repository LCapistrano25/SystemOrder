from abc import ABC, abstractmethod
from Domain.Entities.Payment import Payment


class IPayment(ABC):
    """Contrato de repositório de pagamentos."""
    @abstractmethod
    def get_payment(self, payment_id: int) -> Payment:
        """Obtém um pagamento pelo identificador.

        Args:
            payment_id: Identificador do pagamento.

        Returns:
            Pagamento encontrado.
        """
        raise NotImplementedError

    @abstractmethod
    def add_payment(self, payment: Payment) -> None:
        """Persiste um novo pagamento.

        Args:
            payment: Pagamento a ser adicionado.
        """
        raise NotImplementedError

    @abstractmethod
    def update_payment(self, payment: Payment) -> None:
        """Atualiza um pagamento existente.

        Args:
            payment: Pagamento com dados atualizados.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_payment(self, payment_id: int) -> None:
        """Remove um pagamento pelo identificador.

        Args:
            payment_id: Identificador do pagamento.
        """
        raise NotImplementedError
