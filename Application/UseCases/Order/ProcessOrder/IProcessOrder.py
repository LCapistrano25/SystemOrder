from abc import ABC, abstractmethod

from Application.UseCases.Order.ProcessOrder.ProcessOrderInput import ProcessOrderInput
from Application.UseCases.Order.ProcessOrder.ProcessOrderOutput import ProcessOrderOutput


class IProcessOrder(ABC):
    @abstractmethod
    def execute(self, input_data: ProcessOrderInput) -> ProcessOrderOutput:
        raise NotImplementedError

