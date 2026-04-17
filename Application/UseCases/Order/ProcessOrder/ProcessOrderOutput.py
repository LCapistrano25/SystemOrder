from dataclasses import dataclass


@dataclass(frozen=True)
class ProcessOrderOutput:
    """DTO de saída do processamento de pedidos."""
    order_id: int
    subtotal: float
    discount: float
    freight: float
    interest: float
    total: float
    messages: list[str]
    logs: list[str]
    result_text: str
