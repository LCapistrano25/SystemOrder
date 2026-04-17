import sqlite3
from contextlib import contextmanager

from Infrastructure.Database.IDatabase import IDatabase

class SqliteDatabase(IDatabase):
    """Implementação de banco de dados SQLite com controle transacional simples."""
    def __init__(self, db_path: str):
        """Inicializa o acesso ao banco SQLite.

        Args:
            db_path: Caminho do arquivo .sqlite/.db.
        """
        self._db_path = db_path

    @contextmanager
    def connect(self):
        """Abre uma conexão SQLite e garante commit/rollback ao sair do contexto."""
        connection = sqlite3.connect(self._db_path)
        try:
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA foreign_keys = ON")
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def ensure_schema(self) -> None:
        """Cria tabelas/índices necessários, caso ainda não existam."""
        with self.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS coupons (
                    id INTEGER PRIMARY KEY,
                    code TEXT NOT NULL,
                    discount REAL NOT NULL
                )
                """
            )
            connection.execute(
                """
                CREATE UNIQUE INDEX IF NOT EXISTS idx_coupons_code
                ON coupons (code)
                """
            )

            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    customer_type INTEGER NOT NULL,
                    blocked INTEGER NOT NULL
                )
                """
            )
            connection.execute(
                """
                CREATE UNIQUE INDEX IF NOT EXISTS idx_customers_email
                ON customers (email)
                """
            )

            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL,
                    category INTEGER NOT NULL
                )
                """
            )

            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS payments (
                    id INTEGER PRIMARY KEY,
                    payment_type INTEGER NOT NULL,
                    installments INTEGER NOT NULL
                )
                """
            )

            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS freights (
                    id INTEGER PRIMARY KEY,
                    street TEXT NOT NULL,
                    city TEXT NOT NULL,
                    state TEXT NOT NULL,
                    zip_code TEXT NOT NULL,
                    country TEXT NOT NULL DEFAULT 'BR',
                    total_weight REAL NOT NULL,
                    price REAL NOT NULL,
                    express_delivery INTEGER NOT NULL
                )
                """
            )
            columns = {
                row["name"]
                for row in connection.execute("PRAGMA table_info(freights)").fetchall()
            }
            if "country" not in columns:
                connection.execute(
                    "ALTER TABLE freights ADD COLUMN country TEXT NOT NULL DEFAULT 'BR'"
                )

            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY,
                    customer_id INTEGER NOT NULL,
                    payment_id INTEGER NOT NULL,
                    freight_id INTEGER NOT NULL,
                    coupon_id INTEGER,
                    FOREIGN KEY (customer_id) REFERENCES customers (id),
                    FOREIGN KEY (payment_id) REFERENCES payments (id),
                    FOREIGN KEY (freight_id) REFERENCES freights (id),
                    FOREIGN KEY (coupon_id) REFERENCES coupons (id)
                )
                """
            )
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS order_items (
                    order_id INTEGER NOT NULL,
                    item_id INTEGER NOT NULL,
                    PRIMARY KEY (order_id, item_id),
                    FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
                    FOREIGN KEY (item_id) REFERENCES items (id)
                )
                """
            )
