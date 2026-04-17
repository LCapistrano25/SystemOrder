import re

class Email:
    def __init__(self, value: str):
        self._value = value

    @classmethod
    def create(cls, value: str):
        if not value or not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', value):
            raise ValueError("Email inválido")
        return cls(value)

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        if not isinstance(other, Email):
            return False
        return self._value.lower() == other._value.lower()

    def __hash__(self) -> int:
        return hash(self._value.lower())

    def __str__(self) -> str:
        return self._value
