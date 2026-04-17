from Domain.Entities.Payment import Payment
from Domain.Enums.PaymentType import PaymentType
from Domain.Repositories.Payment.IPayment import IPayment
from Infrastructure.Database.IDatabase import IDatabase

class SqlitePaymentRepository(IPayment):
    def __init__(self, database: IDatabase):
        self._database = database
        self._database.ensure_schema()

    def get_payment(self, payment_id: int) -> Payment:
        with self._database.connect() as connection:
            row = connection.execute(
                "SELECT id, payment_type, installments FROM payments WHERE id = ?",
                (payment_id,),
            ).fetchone()

        if row is None:
            raise ValueError(f"Payment not found: {payment_id}")

        return Payment(
            id=row["id"],
            payment_type=PaymentType(row["payment_type"]),
            installments=row["installments"],
        )

    def add_payment(self, payment: Payment) -> None:
        with self._database.connect() as connection:
            existing = connection.execute(
                "SELECT 1 FROM payments WHERE id = ?",
                (payment.id,),
            ).fetchone()
            if existing is not None:
                raise ValueError(f"Payment already exists: {payment.id}")

            connection.execute(
                "INSERT INTO payments (id, payment_type, installments) VALUES (?, ?, ?)",
                (payment.id, payment.payment_type.value, payment.installments),
            )

    def update_payment(self, payment: Payment) -> None:
        with self._database.connect() as connection:
            result = connection.execute(
                "UPDATE payments SET payment_type = ?, installments = ? WHERE id = ?",
                (payment.payment_type.value, payment.installments, payment.id),
            )

        if result.rowcount == 0:
            raise ValueError(f"Payment not found: {payment.id}")

    def delete_payment(self, payment_id: int) -> None:
        with self._database.connect() as connection:
            result = connection.execute(
                "DELETE FROM payments WHERE id = ?",
                (payment_id,),
            )

        if result.rowcount == 0:
            raise ValueError(f"Payment not found: {payment_id}")
