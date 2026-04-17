from pydantic import BaseModel, EmailStr, Field

class CustomerResponseJson(BaseModel):
    id: int = Field(description="Customer ID")
    name: str = Field(description="Customer name")
    email: EmailStr = Field(description="Customer email")
    customer_type: str = Field(description="Customer type")
    blocked: bool = Field(description="Is customer blocked")
