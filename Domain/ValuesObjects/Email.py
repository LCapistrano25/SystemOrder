import re

class Email:
    """Value Object de e-mail, garantindo formato válido e comparações consistentes."""
    def __init__(self, value: str):
        """Inicializa o value object com um e-mail já validado.

        Args:
            value: E-mail em formato texto (assumido como válido).
        """
        self._value = value

    @classmethod
    def create(cls, value: str):
        """Cria um Email validando seu formato.

        Args:
            value: E-mail em formato texto.

        Returns:
            Instância de Email com o valor validado.

        Raises:
            ValueError: Quando o e-mail estiver ausente ou em formato inválido.
        """
        if not value or not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', value):
            raise ValueError("Email inválido")
        return cls(value)

    @property
    def value(self) -> str:
        """Retorna o valor do e-mail em formato texto."""
        return self._value

    def __eq__(self, other) -> bool:
        """Compara e-mails de forma case-insensitive."""
        if not isinstance(other, Email):
            return False
        return self._value.lower() == other._value.lower()

    def __hash__(self) -> int:
        """Gera hash consistente com a semântica de igualdade case-insensitive."""
        return hash(self._value.lower())

    def __str__(self) -> str:
        """Retorna a representação textual do e-mail."""
        return self._value
