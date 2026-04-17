from Domain.Services.OrderPricing.freight.config import FreightConfig, FreightZoneConfig

class FreightCalculator:
    def __init__(self, config: FreightConfig):
        self._config = config

    def calculate(self, *, country: str, total_weight: float, express_delivery: bool) -> float:
        zone = self._resolve_zone(country)
        base = self._price_by_weight(total_weight, zone)
        return base + (zone.express_surcharge if express_delivery else 0.0)

    def _resolve_zone(self, country: str) -> FreightZoneConfig:
        normalized = (country or "").strip().upper() or self._config.default_country
        return (
            self._config.domestic
            if normalized == self._config.default_country
            else self._config.international
        )

    @staticmethod
    def _price_by_weight(weight: float, zone: FreightZoneConfig) -> float:
        for limit, price in zip(zone.weight_tiers, zone.price_tiers):
            if weight <= limit:
                return float(price)
        return float(zone.price_tiers[-1])