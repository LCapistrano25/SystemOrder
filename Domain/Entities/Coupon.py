import re
from Domain.Entities.base.EntityBase import EntityBase
class Coupon(EntityBase):
    """Entidade de Cupom"""
    def __init__(self, id: int, code: str, discount: float):
        """Inicializa um cupom e valida seus invariantes.

        Args:
            id: Identificador do cupom.
            code: Código do cupom (apenas letras maiúsculas e números).
            discount: Percentual de desconto (não negativo).
        """
        super().__init__(id)
        self.code = code.strip() if code else code
        self.discount = discount
        self._validate()

    def _validate(self):
        """Regras de validação de cupom."""
        if not self.code or not re.match(r'^[A-Z0-9]+$', self.code):
            raise ValueError("Coupon code must contain only uppercase letters and numbers")
        
        if self.discount < 0:
            raise ValueError("Discount cannot be negative")

    def __str__(self):
        """Representação textual do cupom, útil para logs e depuração."""
        return f"Coupon(ID: {self.id}, Code: {self.code}, Discount: {self.discount}%)"
