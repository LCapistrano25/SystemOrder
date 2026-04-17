from Domain.Entities.Freight import Freight
from Domain.Repositories.Freight.IFreight import IFreight
from Domain.ValuesObjects.Address import Address
from Infrastructure.Database.IDatabase import IDatabase


class SqliteFreightRepository(IFreight):
    """Repositório SQLite para persistência e consulta de fretes."""
    def __init__(self, database: IDatabase):
        """Inicializa o repositório e garante o schema.

        Args:
            database: Abstração de banco de dados usada para conexão/transações.
        """
        self._database = database
        self._database.ensure_schema()

    def get_freight(self, freight_id: int) -> Freight:
        """Obtém um frete pelo id.

        Raises:
            ValueError: Quando o frete não existir.
        """
        with self._database.connect() as connection:
            row = connection.execute(
                """
                SELECT
                    id,
                    street,
                    city,
                    state,
                    zip_code,
                    country,
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
            country=row["country"],
        )
        return Freight(
            id=row["id"],
            address=address,
            total_weight=row["total_weight"],
            price=row["price"],
            express_delivery=bool(row["express_delivery"]),
        )

    def add_freight(self, freight: Freight) -> None:
        """Adiciona um novo frete.

        Raises:
            ValueError: Quando já existir frete com o mesmo id.
        """
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
                    country,
                    total_weight,
                    price,
                    express_delivery
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    freight.id,
                    freight.address.street,
                    freight.address.city,
                    freight.address.state,
                    freight.address.zip_code,
                    freight.address.country,
                    freight.total_weight,
                    freight.price,
                    1 if freight.express_delivery else 0,
                ),
            )

    def update_freight(self, freight: Freight) -> None:
        """Atualiza um frete existente.

        Raises:
            ValueError: Quando o frete não existir.
        """
        with self._database.connect() as connection:
            result = connection.execute(
                """
                UPDATE freights
                SET
                    street = ?,
                    city = ?,
                    state = ?,
                    zip_code = ?,
                    country = ?,
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
                    freight.address.country,
                    freight.total_weight,
                    freight.price,
                    1 if freight.express_delivery else 0,
                    freight.id,
                ),
            )

        if result.rowcount == 0:
            raise ValueError(f"Freight not found: {freight.id}")

    def delete_freight(self, freight_id: int) -> None:
        """Remove um frete pelo id.

        Raises:
            ValueError: Quando o frete não existir.
        """
        with self._database.connect() as connection:
            result = connection.execute(
                "DELETE FROM freights WHERE id = ?",
                (freight_id,),
            )

        if result.rowcount == 0:
            raise ValueError(f"Freight not found: {freight_id}")
