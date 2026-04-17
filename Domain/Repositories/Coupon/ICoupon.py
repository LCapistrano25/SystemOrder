from abc import ABC, abstractmethod
from Domain.Entities.Coupon import Coupon

class ICoupon(ABC):
    """Contrato de repositório de cupons."""
    @abstractmethod
    def get_coupon(self, coupon_id: int) -> Coupon:
        """Obtém um cupom pelo identificador.

        Args:
            coupon_id: Identificador do cupom.

        Returns:
            Cupom encontrado.
        """
        raise NotImplementedError

    @abstractmethod
    def add_coupon(self, coupon: Coupon) -> None:
        """Persiste um novo cupom.

        Args:
            coupon: Cupom a ser adicionado.
        """
        raise NotImplementedError

    @abstractmethod
    def update_coupon(self, coupon: Coupon) -> None:
        """Atualiza um cupom existente.

        Args:
            coupon: Cupom com dados atualizados.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_coupon(self, coupon_id: int) -> None:
        """Remove um cupom pelo identificador.

        Args:
            coupon_id: Identificador do cupom.
        """
        raise NotImplementedError
