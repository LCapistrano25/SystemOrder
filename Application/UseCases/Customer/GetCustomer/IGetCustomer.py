from abc import ABC, abstractmethod

from Application.UseCases.Customer.CustomerInput import CustomerInput
from Application.UseCases.Customer.CustomerOutput import CustomerOutput

class IGetCustomer(ABC):
    """Contrato para consulta/obtenção de cliente na camada de aplicação."""
    
    @abstractmethod
    def execute(self, customer: CustomerInput) -> CustomerOutput:
        """Executa a obtenção de um cliente a partir de um input.

        Args:
            customer: Critério/dados de entrada para a consulta.

        Returns:
            Dados do cliente encontrado no formato de saída.
        """
        raise NotImplementedError
