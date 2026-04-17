from abc import ABC, abstractmethod

from Application.UseCases.Customer.CustomerInput import CustomerInput
from Application.UseCases.Customer.CustomerOutput import CustomerOutput

class ICreateCustomer(ABC):
    """Contrato do caso de uso de criação de cliente."""
    
    @abstractmethod
    def execute(self, customer: CustomerInput) -> CustomerOutput:
        """Executa a criação de cliente.

        Args:
            customer: Dados de entrada para criação do cliente.

        Returns:
            Dados do cliente criado.
        """
        raise NotImplementedError
