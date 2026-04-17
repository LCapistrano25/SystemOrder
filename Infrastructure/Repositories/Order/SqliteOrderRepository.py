from Domain.Entities.Order import Order
from Domain.Entities.Customer import Customer
from Domain.Entities.Item import Item
from Domain.Entities.Payment import Payment
from Domain.Entities.Freight import Freight
from Domain.Entities.Coupon import Coupon
from Domain.Enums.Category import Category
from Domain.Enums.CustomerType import CustomerType
from Domain.Enums.PaymentType import PaymentType
from Domain.Repositories.Order.IOrder import IOrder
from Infrastructure.Database.IDatabase import IDatabase
from Domain.ValuesObjects.Address import Address


class SqliteOrderRepository(IOrder):
    """Repositório SQLite para persistência e consulta de pedidos."""
    def __init__(self, database: IDatabase):
        """Inicializa o repositório e garante o schema.

        Args:
            database: Abstração de banco de dados usada para conexão/transações.
        """
        self._database = database
        self._database.ensure_schema()

    def get_order(self, order_id: int) -> Order:
        """Obtém um pedido agregado (cliente, itens, pagamento, frete e cupom).

        Raises:
            ValueError: Quando o pedido não existir ou dados estiverem incompletos.
        """
        with self._database.connect() as connection:
            order_row = connection.execute(
                """
                SELECT id,
                       customer_id,
                       payment_id,
                       freight_id,
                       coupon_id
                FROM orders
                WHERE id = ?
                """,
                (order_id,),
            ).fetchone()

            if order_row is None:
                raise ValueError(f"Order not found: {order_id}")

            customer_row = connection.execute(
                "SELECT id, name, email, customer_type, blocked FROM customers WHERE id = ?",
                (order_row["customer_id"],),
            ).fetchone()
            payment_row = connection.execute(
                "SELECT id, payment_type, installments FROM payments WHERE id = ?",
                (order_row["payment_id"],),
            ).fetchone()
            freight_row = connection.execute(
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
                (order_row["freight_id"],),
            ).fetchone()
            coupon_row = None
            if order_row["coupon_id"] is not None:
                coupon_row = connection.execute(
                    "SELECT id, code, discount FROM coupons WHERE id = ?",
                    (order_row["coupon_id"],),
                ).fetchone()

            item_rows = connection.execute(
                """
                SELECT i.id, i.name, i.price, i.quantity, i.category
                FROM items i
                JOIN order_items oi ON oi.item_id = i.id
                WHERE oi.order_id = ?
                """,
                (order_id,),
            ).fetchall()

        if customer_row is None or payment_row is None or freight_row is None:
            raise ValueError(f"Incomplete data for order: {order_id}")

        customer = Customer(
            id=customer_row["id"],
            name=customer_row["name"],
            email=customer_row["email"],
            customer_type=CustomerType(customer_row["customer_type"]),
        )
        if bool(customer_row["blocked"]):
            customer.block()

        payment = Payment(
            id=payment_row["id"],
            payment_type=PaymentType(payment_row["payment_type"]),
            installments=payment_row["installments"],
        )

        address = Address.create(
            street=freight_row["street"],
            city=freight_row["city"],
            state=freight_row["state"],
            zip_code=freight_row["zip_code"],
            country=freight_row["country"],
        )
        freight = Freight(
            id=freight_row["id"],
            address=address,
            total_weight=freight_row["total_weight"],
            price=freight_row["price"],
            express_delivery=bool(freight_row["express_delivery"]),
        )

        coupon = None
        if coupon_row is not None:
            coupon = Coupon(
                id=coupon_row["id"],
                code=coupon_row["code"],
                discount=coupon_row["discount"],
            )

        items = [
            Item(
                id=row["id"],
                name=row["name"],
                price=row["price"],
                quantity=row["quantity"],
                category=Category(row["category"]),
            )
            for row in item_rows
        ]

        return Order(
            id=order_row["id"],
            customer=customer,
            items=items,
            payment=payment,
            freight=freight,
            coupon=coupon,
        )

    def add_order(self, order: Order) -> None:
        """Adiciona um novo pedido e suas associações de itens.

        Raises:
            ValueError: Quando já existir pedido com o mesmo id.
        """
        with self._database.connect() as connection:
            existing = connection.execute(
                "SELECT 1 FROM orders WHERE id = ?",
                (order.id,),
            ).fetchone()
            if existing is not None:
                raise ValueError(f"Order already exists: {order.id}")

            connection.execute(
                """
                INSERT INTO orders (
                    id,
                    customer_id,
                    payment_id,
                    freight_id,
                    coupon_id
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    order.id,
                    order.customer.id,
                    order.payment.id,
                    order.freight.id,
                    order.coupon.id if order.coupon is not None else None,
                ),
            )

            for item in order.items:
                connection.execute(
                    "INSERT INTO order_items (order_id, item_id) VALUES (?, ?)",
                    (order.id, item.id),
                )

    def update_order(self, order: Order) -> None:
        """Atualiza um pedido e recria o vínculo de itens.

        Raises:
            ValueError: Quando o pedido não existir.
        """
        with self._database.connect() as connection:
            result = connection.execute(
                """
                UPDATE orders
                SET
                    customer_id = ?,
                    payment_id = ?,
                    freight_id = ?,
                    coupon_id = ?
                WHERE id = ?
                """,
                (
                    order.customer.id,
                    order.payment.id,
                    order.freight.id,
                    order.coupon.id if order.coupon is not None else None,
                    order.id,
                ),
            )

            connection.execute(
                "DELETE FROM order_items WHERE order_id = ?",
                (order.id,),
            )
            for item in order.items:
                connection.execute(
                    "INSERT INTO order_items (order_id, item_id) VALUES (?, ?)",
                    (order.id, item.id),
                )

        if result.rowcount == 0:
            raise ValueError(f"Order not found: {order.id}")

    def delete_order(self, order_id: int) -> None:
        """Remove um pedido e seus itens associados.

        Raises:
            ValueError: Quando o pedido não existir.
        """
        with self._database.connect() as connection:
            connection.execute(
                "DELETE FROM order_items WHERE order_id = ?",
                (order_id,),
            )
            result = connection.execute(
                "DELETE FROM orders WHERE id = ?",
                (order_id,),
            )

        if result.rowcount == 0:
            raise ValueError(f"Order not found: {order_id}")
