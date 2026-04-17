from Domain.Services.OrderPricing.freight.config import FreightConfig, FreightZoneConfig

class FreightCalculator:
    """Calcula o valor do frete a partir de regras configuráveis por zona."""
    def __init__(self, config: FreightConfig):
        """Inicializa a calculadora de frete.

        Args:
            config: Configurações de faixas e valores de frete.
        """
        self._config = config

    def calculate(self, *, country: str, total_weight: float, express_delivery: bool) -> float:
        """Calcula o frete considerando país, peso total e entrega expressa."""
        zone = self._resolve_zone(country)
        base = self._price_by_weight(total_weight, zone)
        return base + (zone.express_surcharge if express_delivery else 0.0)

    def _resolve_zone(self, country: str) -> FreightZoneConfig:
        """Resolve a zona (nacional/internacional) a partir do país."""
        normalized = (country or "").strip().upper() or self._config.default_country
        return (
            self._config.domestic
            if normalized == self._config.default_country
            else self._config.international
        )

    @staticmethod
    def _price_by_weight(weight: float, zone: FreightZoneConfig) -> float:
        """Seleciona o preço base com base no peso e nas faixas configuradas."""
        for limit, price in zip(zone.weight_tiers, zone.price_tiers):
            if weight <= limit:
                return float(price)
        return float(zone.price_tiers[-1])
