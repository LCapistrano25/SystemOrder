from enum import IntEnum

class CustomerTypeJson(IntEnum):
    VIP = 1
    PREMIUM = 2
    STANDARD = 3
    NEW = 4

    @staticmethod
    def to_json(value: "CustomerTypeJson") -> str:
        return value.name

    @staticmethod
    def from_json(value: str | int) -> "CustomerTypeJson":
        if isinstance(value, int):
            return CustomerTypeJson(value)
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Invalid customer_type")
        return CustomerTypeJson[value.strip().upper()]
