import sqlite3

from Domain.Entities.Customer import Customer
from Domain.Enums.CustomerType import CustomerType
from Domain.Repositories.Customer.ICustomer import ICustomer
from Infrastructure.Database.IDatabase import IDatabase


class SqliteCustomerRepository(ICustomer):
    """Repositório SQLite para persistência e consulta de clientes."""
    def __init__(self, database: IDatabase):
        """Inicializa o repositório e garante o schema.

        Args:
            database: Abstração de banco de dados usada para conexão/transações.
        """
        self._database = database
        self._database.ensure_schema()

    def get_customer(self, customer_id: int) -> Customer:
        """Obtém um cliente por id.

        Raises:
            ValueError: Quando o cliente não existir.
        """
        with self._database.connect() as connection:
            row = connection.execute(
                "SELECT id, name, email, customer_type, blocked FROM customers WHERE id = ?",
                (customer_id,),
            ).fetchone()

        if row is None:
            raise ValueError(f"Customer not found: {customer_id}")

        customer = Customer(
            id=row["id"],
            name=row["name"],
            email=row["email"],
            customer_type=CustomerType(row["customer_type"]),
        )
        if bool(row["blocked"]):
            customer.block()
        return customer

    def list_customers(self) -> list[Customer]:
        """Lista clientes ordenados por id."""
        with self._database.connect() as connection:
            rows = connection.execute(
                "SELECT id, name, email, customer_type, blocked FROM customers ORDER BY id",
            ).fetchall()

        customers: list[Customer] = []
        for row in rows:
            customer = Customer(
                id=row["id"],
                name=row["name"],
                email=row["email"],
                customer_type=CustomerType(row["customer_type"]),
            )
            if bool(row["blocked"]):
                customer.block()
            customers.append(customer)
        return customers

    def add_customer(self, customer: Customer) -> None:
        """Adiciona um cliente, atribuindo id quando necessário.

        Raises:
            ValueError: Quando existir conflito de e-mail ou id.
        """
        with self._database.connect() as connection:
            existing_email = connection.execute(
                "SELECT 1 FROM customers WHERE email = ?",
                (customer.email.value,),
            ).fetchone()
            if existing_email is not None:
                raise ValueError(f"Customer already exists with email: {customer.email.value}")

            if customer.id is None:
                try:
                    cursor = connection.execute(
                        "INSERT INTO customers (name, email, customer_type, blocked) VALUES (?, ?, ?, ?)",
                        (
                            customer.name,
                            customer.email.value,
                            customer.customer_type.value,
                            1 if customer.blocked else 0,
                        ),
                    )
                except sqlite3.IntegrityError as exc:
                    if "customers.email" in str(exc):
                        raise ValueError(f"Customer already exists with email: {customer.email.value}") from exc
                    raise
                customer.id = int(cursor.lastrowid)
                return

            existing = connection.execute(
                "SELECT 1 FROM customers WHERE id = ?",
                (customer.id,),
            ).fetchone()
            if existing is not None:
                raise ValueError(f"Customer already exists: {customer.id}")

            try:
                connection.execute(
                    "INSERT INTO customers (id, name, email, customer_type, blocked) VALUES (?, ?, ?, ?, ?)",
                    (
                        customer.id,
                        customer.name,
                        customer.email.value,
                        customer.customer_type.value,
                        1 if customer.blocked else 0,
                    ),
                )
            except sqlite3.IntegrityError as exc:
                if "customers.email" in str(exc):
                    raise ValueError(f"Customer already exists with email: {customer.email.value}") from exc
                raise

    def update_customer(self, customer: Customer) -> None:
        """Atualiza um cliente existente.

        Raises:
            ValueError: Quando o cliente não existir ou houver conflito de e-mail.
        """
        with self._database.connect() as connection:
            existing_email = connection.execute(
                "SELECT 1 FROM customers WHERE email = ? AND id != ?",
                (customer.email.value, customer.id),
            ).fetchone()
            if existing_email is not None:
                raise ValueError(f"Customer already exists with email: {customer.email.value}")

            try:
                result = connection.execute(
                    "UPDATE customers SET name = ?, email = ?, customer_type = ?, blocked = ? WHERE id = ?",
                    (
                        customer.name,
                        customer.email.value,
                        customer.customer_type.value,
                        1 if customer.blocked else 0,
                        customer.id,
                    ),
                )
            except sqlite3.IntegrityError as exc:
                if "customers.email" in str(exc):
                    raise ValueError(f"Customer already exists with email: {customer.email.value}") from exc
                raise

        if result.rowcount == 0:
            raise ValueError(f"Customer not found: {customer.id}")

    def delete_customer(self, customer_id: int) -> None:
        """Remove um cliente por id.

        Raises:
            ValueError: Quando o cliente não existir.
        """
        with self._database.connect() as connection:
            result = connection.execute(
                "DELETE FROM customers WHERE id = ?",
                (customer_id,),
            )

        if result.rowcount == 0:
            raise ValueError(f"Customer not found: {customer_id}")
