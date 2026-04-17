from dataclasses import dataclass


@dataclass(frozen=True)
class ProcessOrderInput:
    """DTO de entrada para o processamento de pedidos."""
    order_id: int
    send_email: bool = False
    save_log: bool = False
