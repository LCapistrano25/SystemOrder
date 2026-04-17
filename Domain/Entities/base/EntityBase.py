from abc import ABC, abstractmethod

class EntityBase(ABC):
    """Classe base para entidades do domínio (com identidade)."""
    @abstractmethod
    def __init__(self, id: int):
        """Inicializa a entidade base com um identificador.

        Args:
            id: Identificador da entidade.
        """
        self.id = id
