from dataclasses import dataclass


@dataclass(frozen=True)
class CustomerInput:
    name: str
    email: str
    customer_type: int
    blocked: bool = False

