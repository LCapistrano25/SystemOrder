from dataclasses import dataclass


@dataclass
class AddressResponseJson:
    street: str
    city: str
    state: str
    zip_code: str

    @classmethod
    def from_payload(cls, payload: dict) -> "AddressResponseJson":
        return cls(
            street=payload["street"],
            city=payload["city"],
            state=payload["state"],
            zip_code=payload["zip_code"],
        )

    def to_dict(self) -> dict:
        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
        }
