from pydantic import BaseModel, EmailStr, Field

class CustomerRequestJson(BaseModel):
    name: str = Field(min_length=2, description="Customer name")
    email: EmailStr = Field(description="Customer email")
    customer_type: int | str = Field(description="Customer type")
    blocked: bool = Field(description="Is customer blocked", default=False)
