from pydantic import BaseModel, Field
class PaymentResponseJson(BaseModel):
    id: int = Field(description="ID da pagamento")
    payment_type: str = Field(description="Tipo de pagamento")
    installments: int = Field(description="Número de parcelas")
