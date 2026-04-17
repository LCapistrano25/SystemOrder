from abc import ABC, abstractmethod

class IDatabase(ABC):
    """Contrato de acesso a banco de dados (conexão e bootstrap de schema)."""

    @abstractmethod
    def connect(self):
        """Abre um contexto de conexão com o banco de dados."""
        raise NotImplementedError

    @abstractmethod
    def ensure_schema(self) -> None:
        """Garante que o schema/tabelas existam no banco de dados."""
        raise NotImplementedError
