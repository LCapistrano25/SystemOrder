from pydantic import BaseModel, Field

class OrderRequest(BaseModel):
    id: int = Field(description="ID da pedido")
    customer_id: int = Field(description="ID do cliente")
    item_ids: list[int] = Field(description="IDs dos items", items_type=list("[int]"))
    payment_id: int = Field(description="ID do pagamento")
    freight_id: int = Field(description="ID do frete")
    coupon_id: int | None = Field(description="ID do cupom", default=None)