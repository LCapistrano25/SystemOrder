from abc import ABC, abstractmethod

class EntityBase(ABC):
    @abstractmethod
    def __init__(self, id: int):
        self.id = id
