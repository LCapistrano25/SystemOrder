"""Configuração de frete (faixas de peso, preços e adicional para entrega expressa)."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class FreightZoneConfig:
    """Configuração de uma zona de frete (faixas de peso e valores)."""
    weight_tiers: tuple[float, ...]
    price_tiers: tuple[float, ...]
    express_surcharge: float


@dataclass(frozen=True)
class FreightConfig:
    """Configuração completa de frete para cenários nacional e internacional."""
    default_country: str = "BR"
    domestic: FreightZoneConfig = field(
        default_factory=lambda: FreightZoneConfig(
            weight_tiers=(1.0, 5.0, 10.0),
            price_tiers=(10.0, 25.0, 40.0, 70.0),
            express_surcharge=30.0,
        )
    )
    international: FreightZoneConfig = field(
        default_factory=lambda: FreightZoneConfig(
            weight_tiers=(1.0, 5.0),
            price_tiers=(50.0, 80.0, 120.0),
            express_surcharge=70.0,
        )
    )

