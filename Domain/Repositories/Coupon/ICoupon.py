from abc import ABC, abstractmethod
from Domain.Entities.Coupon import Coupon

class ICoupon(ABC):
    @abstractmethod
    def get_coupon(self, coupon_id: int) -> Coupon:
        pass

    @abstractmethod
    def add_coupon(self, coupon: Coupon) -> None:
        pass

    @abstractmethod
    def update_coupon(self, coupon: Coupon) -> None:
        pass

    @abstractmethod
    def delete_coupon(self, coupon_id: int) -> None:
        pass
