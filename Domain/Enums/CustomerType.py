from enum import Enum

class CustomerType(Enum):
    """Enum com tipos de cliente usados nas regras de negócio."""
    VIP = 1
    PREMIUM = 2
    STANDARD = 3
    NEW = 4
