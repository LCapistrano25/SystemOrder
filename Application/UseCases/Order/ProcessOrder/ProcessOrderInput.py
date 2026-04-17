from dataclasses import dataclass


@dataclass(frozen=True)
class ProcessOrderInput:
    order_id: int
    send_email: bool = False
    save_log: bool = False

