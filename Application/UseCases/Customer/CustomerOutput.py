from dataclasses import dataclass


@dataclass(frozen=True)
class CustomerOutput:
    """DTO de saída para casos de uso relacionados a cliente."""
    id: int
    name: str
    email: str
    customer_type: str
    blocked: bool
