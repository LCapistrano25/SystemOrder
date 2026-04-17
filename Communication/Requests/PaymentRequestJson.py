from pydantic import BaseModel, Field
from Communication.Enums.PaymentTypeJson import PaymentTypeJson

class PaymentRequest(BaseModel):
    id: int = Field(description="ID do pagamento")
    payment_type: PaymentTypeJson = Field(description="Tipo de pagamento", enum=PaymentTypeJson)
    installments: int = Field(description="Quantidade de parcelas")
