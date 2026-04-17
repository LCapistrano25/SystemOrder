from abc import ABC, abstractmethod

class IDatabase(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def ensure_schema(self) -> None:
        pass