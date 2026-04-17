from enum import IntEnum


class CategoryJson(IntEnum):
    FOOD = 1
    IMPORTED = 2

    @staticmethod
    def to_json(value: "CategoryJson") -> str:
        return value.name

    @staticmethod
    def from_json(value: str | int) -> "CategoryJson":
        if isinstance(value, int):
            return CategoryJson(value)
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Invalid category")
        return CategoryJson[value.strip().upper()]
