from Domain.Enums.PaymentType import PaymentType
from Domain.Entities.base.EntityBase import EntityBase

class Payment(EntityBase):
    def __init__(self, id: int, payment_type: PaymentType, installments: int):
        super().__init__(id)
        self.payment_type = payment_type
        self.installments = installments
        self._validate()

    def _validate(self):
        if not isinstance(self.payment_type, PaymentType):
            raise ValueError("Invalid payment type")
        if self.payment_type == PaymentType.CARD:
            if self.installments <= 0:
                raise ValueError("Installments must be greater than zero")
        else:
            if self.installments != 1:
                raise ValueError("Installments must be 1 for non-card payments")

    def __str__(self):
        return f"Payment(ID: {self.id}, Payment Type: {self.payment_type.name}, Installments: {self.installments})"
