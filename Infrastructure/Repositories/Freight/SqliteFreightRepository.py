from Domain.Entities.Freight import Freight
from Domain.Repositories.Freight.IFreight import IFreight
from Domain.ValuesObjects.Address import Address
from Infrastructure.Database.IDatabase import IDatabase


class SqliteFreightRepository(IFreight):
    def __init__(self, database: IDatabase):
        self._database = database
        self._database.ensure_schema()

    def get_freight(self, freight_id: int) -> Freight:
        with self._database.connect() as connection:
            row = connection.execute(
                """
                SELECT
                    id,
                    street,
                    city,
                    state,
                    zip_code,
                    total_weight,
                    price,
                    express_delivery
                FROM freights
                WHERE id = ?
                """,
                (freight_id,),
            ).fetchone()

        if row is None:
            raise ValueError(f"Freight not found: {freight_id}")

        address = Address.create(
            street=row["street"],
            city=row["city"],
            state=row["state"],
            zip_code=row["zip_code"],
        )
        return Freight(
            id=row["id"],
            address=address,
            total_weight=row["total_weight"],
            price=row["price"],
            express_delivery=bool(row["express_delivery"]),
        )

    def add_freight(self, freight: Freight) -> None:
        with self._database.connect() as connection:
            existing = connection.execute(
                "SELECT 1 FROM freights WHERE id = ?",
                (freight.id,),
            ).fetchone()
            if existing is not None:
                raise ValueError(f"Freight already exists: {freight.id}")

            connection.execute(
                """
                INSERT INTO freights (
                    id,
                    street,
                    city,
                    state,
                    zip_code,
                    total_weight,
                    price,
                    express_delivery
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    freight.id,
                    freight.address.street,
                    freight.address.city,
                    freight.address.state,
                    freight.address.zip_code,
                    freight.total_weight,
                    freight.price,
                    1 if freight.express_delivery else 0,
                ),
            )

    def update_freight(self, freight: Freight) -> None:
        with self._database.connect() as connection:
            result = connection.execute(
                """
                UPDATE freights
                SET
                    street = ?,
                    city = ?,
                    state = ?,
                    zip_code = ?,
                    total_weight = ?,
                    price = ?,
                    express_delivery = ?
                WHERE id = ?
                """,
                (
                    freight.address.street,
                    freight.address.city,
                    freight.address.state,
                    freight.address.zip_code,
                    freight.total_weight,
                    freight.price,
                    1 if freight.express_delivery else 0,
                    freight.id,
                ),
            )

        if result.rowcount == 0:
            raise ValueError(f"Freight not found: {freight.id}")

    def delete_freight(self, freight_id: int) -> None:
        with self._database.connect() as connection:
            result = connection.execute(
                "DELETE FROM freights WHERE id = ?",
                (freight_id,),
            )

        if result.rowcount == 0:
            raise ValueError(f"Freight not found: {freight_id}")
