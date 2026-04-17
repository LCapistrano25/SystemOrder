from abc import ABC, abstractmethod

from Application.UseCases.Customer.CustomerInput import CustomerInput
from Application.UseCases.Customer.CustomerOutput import CustomerOutput

class ICreateCustomer(ABC):
    
    @abstractmethod
    def execute(self, customer: CustomerInput) -> CustomerOutput:
        pass
