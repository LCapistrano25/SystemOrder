class Address:
    """Value Object de endereço, com validação básica por país."""
    def __init__(self, street: str, city: str, state: str, zip_code: str, country: str = "BR"):
        """Inicializa o value object com dados de endereço.

        Args:
            street: Logradouro.
            city: Cidade.
            state: Estado/UF.
            zip_code: CEP/código postal.
            country: País (padrão BR).
        """
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    @classmethod
    def create(cls, street: str, city: str, state: str, zip_code: str, country: str = "BR"):
        """Cria um Address validando seus campos.

        Raises:
            ValueError: Quando algum campo estiver ausente ou inválido.
        """
        if not cls._validate(street, city, state, zip_code, country):
            raise ValueError("Endereço inválido")
        return cls(street, city, state, zip_code, country)

    @staticmethod
    def _validate(street: str, city: str, state: str, zip_code: str, country: str) -> bool:
        """Valida campos do endereço conforme regras simples por país."""
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
        """Compara endereços por igualdade de valores."""
        if not isinstance(other, Address):
            return False
        return (self.street == other.street and
                self.city == other.city and
                self.state == other.state and
                self.zip_code == other.zip_code and
                self.country == other.country)

    def __hash__(self) -> int:
        """Gera hash consistente com a semântica de igualdade."""
        return hash((self.street, self.city, self.state, self.zip_code, self.country))

    def __str__(self) -> str:
        """Retorna a representação textual do endereço."""
        return f"{self.street}, {self.city}, {self.state} {self.zip_code} ({self.country})"
