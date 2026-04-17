from pydantic import BaseModel, Field


class ItemResponseJson(BaseModel):
    id: int = Field(description="ID do item")
    name: str = Field(description="Nome do item")
    price: float = Field(description="Preço unitário em reais")
    quantity: int = Field(description="Quantidade")
    category: str = Field(description="Categoria do item")