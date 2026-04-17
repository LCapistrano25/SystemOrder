from Domain.Entities.Item import Item
from Domain.Enums.Category import Category
from Domain.Repositories.Item.IItem import IItem
from Infrastructure.Database.IDatabase import IDatabase

class SqliteItemRepository(IItem):
    """Repositório SQLite para persistência e consulta de itens."""
    def __init__(self, database: IDatabase):
        """Inicializa o repositório e garante o schema.

        Args:
            database: Abstração de banco de dados usada para conexão/transações.
        """
        self._database = database
        self._database.ensure_schema()

    def get_item(self, item_id: int) -> Item:
        """Obtém um item pelo id.

        Raises:
            ValueError: Quando o item não existir.
        """
        with self._database.connect() as connection:
            row = connection.execute(
                "SELECT id, name, price, quantity, category FROM items WHERE id = ?",
                (item_id,),
            ).fetchone()

        if row is None:
            raise ValueError(f"Item not found: {item_id}")

        return Item(
            id=row["id"],
            name=row["name"],
            price=row["price"],
            quantity=row["quantity"],
            category=Category(row["category"]),
        )

    def add_item(self, item: Item) -> None:
        """Adiciona um novo item.

        Raises:
            ValueError: Quando já existir item com o mesmo id.
        """
        with self._database.connect() as connection:
            existing = connection.execute(
                "SELECT 1 FROM items WHERE id = ?",
                (item.id,),
            ).fetchone()
            if existing is not None:
                raise ValueError(f"Item already exists: {item.id}")

            connection.execute(
                "INSERT INTO items (id, name, price, quantity, category) VALUES (?, ?, ?, ?, ?)",
                (item.id, item.name, item.price, item.quantity, item.category.value),
            )

    def update_item(self, item: Item) -> None:
        """Atualiza um item existente.

        Raises:
            ValueError: Quando o item não existir.
        """
        with self._database.connect() as connection:
            result = connection.execute(
                "UPDATE items SET name = ?, price = ?, quantity = ?, category = ? WHERE id = ?",
                (item.name, item.price, item.quantity, item.category.value, item.id),
            )

        if result.rowcount == 0:
            raise ValueError(f"Item not found: {item.id}")

    def delete_item(self, item_id: int) -> None:
        """Remove um item pelo id.

        Raises:
            ValueError: Quando o item não existir.
        """
        with self._database.connect() as connection:
            result = connection.execute(
                "DELETE FROM items WHERE id = ?",
                (item_id,),
            )

        if result.rowcount == 0:
            raise ValueError(f"Item not found: {item_id}")
