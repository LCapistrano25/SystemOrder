from pydantic import BaseModel, Field
from Communication.Enums.CategoryJson import CategoryJson

class ItemRequest(BaseModel):
    id: int = Field(description="ID do item")
    name: str = Field(description="Nome do item")
    price: float = Field(description="Preço do item")
    quantity: int = Field(description="Quantidade do item")
    category: CategoryJson = Field(description="Categoria do item", enum=CategoryJson)
