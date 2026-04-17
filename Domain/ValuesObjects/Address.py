class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    @classmethod
    def create(cls, street: str, city: str, state: str, zip_code: str):
        if not cls._validate(street, city, state, zip_code):
            raise ValueError("Endereço inválido")
        return cls(street, city, state, zip_code)

    @staticmethod
    def _validate(street: str, city: str, state: str, zip_code: str) -> bool:
        if not street or not city or not state or not zip_code:
            return False
        cleaned = zip_code.replace("-", "")
        if len(cleaned) != 8 or not cleaned.isdigit():
            return False
        return True

    def __eq__(self, other) -> bool:
        if not isinstance(other, Address):
            return False
        return (self.street == other.street and
                self.city == other.city and
                self.state == other.state and
                self.zip_code == other.zip_code)

    def __hash__(self) -> int:
        return hash((self.street, self.city, self.state, self.zip_code))

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"
