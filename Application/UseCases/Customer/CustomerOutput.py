from dataclasses import dataclass


@dataclass(frozen=True)
class CustomerOutput:
    id: int
    name: str
    email: str
    customer_type: str
    blocked: bool

