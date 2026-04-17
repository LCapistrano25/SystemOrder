from pydantic import BaseModel, Field

from Communication.Responses.AddressResponseJson import AddressResponseJson

class FreightResponseJson(BaseModel):
    id: int = Field(description="ID do frete")
    address: AddressResponseJson = Field(description="Endereço")
    total_weight: float = Field(description="Peso total em kg")
    price: float = Field(description="Preço total em reais")
    express_delivery: bool = Field(description="É entrega expressa")