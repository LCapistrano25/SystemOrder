from pydantic import BaseModel, Field



class AddressResponseJson(BaseModel):
    street: str = Field(description="Rua")
    city: str = Field(description="Cidade")
    state: str = Field(description="Estado")
    zip_code: str = Field(description="Código postal")
    country: str = Field(description="País", default="BR")