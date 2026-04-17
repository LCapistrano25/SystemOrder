from dataclasses import dataclass


@dataclass(frozen=True)
class CustomerInput:
    """DTO de entrada para casos de uso relacionados a cliente."""
    name: str
    email: str
    customer_type: int
    blocked: bool = False
