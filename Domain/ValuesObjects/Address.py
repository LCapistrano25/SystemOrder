class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str, country: str = "BR"):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    @classmethod
    def create(cls, street: str, city: str, state: str, zip_code: str, country: str = "BR"):
        if not cls._validate(street, city, state, zip_code, country):
            raise ValueError("Endereço inválido")
        return cls(street, city, state, zip_code, country)

    @staticmethod
    def _validate(street: str, city: str, state: str, zip_code: str, country: str) -> bool:
        if not street or not city or not state or not zip_code or not country:
            return False
        if country.strip().upper() == "BR":
            cleaned = zip_code.replace("-", "")
            if len(cleaned) != 8 or not cleaned.isdigit():
                return False
        else:
            if len(zip_code.strip()) < 2:
                return False
        return True

    def __eq__(self, other) -> bool:
        if not isinstance(other, Address):
            return False
        return (self.street == other.street and
                self.city == other.city and
                self.state == other.state and
                self.zip_code == other.zip_code and
                self.country == other.country)

    def __hash__(self) -> int:
        return hash((self.street, self.city, self.state, self.zip_code, self.country))

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.zip_code} ({self.country})"
