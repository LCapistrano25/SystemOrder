from abc import ABC, abstractmethod

from Application.UseCases.Order.ProcessOrder.ProcessOrderInput import ProcessOrderInput
from Application.UseCases.Order.ProcessOrder.ProcessOrderOutput import ProcessOrderOutput


class IProcessOrder(ABC):
    """Contrato do caso de uso de processamento de pedidos."""
    @abstractmethod
    def execute(self, input_data: ProcessOrderInput) -> ProcessOrderOutput:
        """Processa um pedido e retorna o resultado do processamento.

        Args:
            input_data: Parâmetros de processamento do pedido.

        Returns:
            Resultado do processamento do pedido.
        """
        raise NotImplementedError

