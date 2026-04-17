from pydantic import BaseModel, Field
class CouponRequest(BaseModel):
    id: int = Field(description="ID do cupom")
    code: str = Field(description="Código do cupom")
    discount: float = Field(description="Desconto em percentual")