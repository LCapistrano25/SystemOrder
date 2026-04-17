from pydantic import BaseModel, Field

class FreightRequest(BaseModel):
    id: int = Field(description="ID do frete")
    street: str = Field(description="Rua")
    city: str = Field(description="Cidade")
    state: str = Field(description="Estado")
    zip_code: str = Field(description="Código postal")
    country: str = Field(description="País")
    total_weight: float = Field(description="Peso total")
    price: float = Field(description="Preço")
    express_delivery: bool = Field(description="Entrega expressa")
