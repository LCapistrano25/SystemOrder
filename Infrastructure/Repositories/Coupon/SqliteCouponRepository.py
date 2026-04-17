from Domain.Entities.Coupon import Coupon
from Domain.Repositories.Coupon.ICoupon import ICoupon
from Infrastructure.Database.SqliteDatabase import SqliteDatabase


class SqliteCouponRepository(ICoupon):
    def __init__(self, database: SqliteDatabase):
        self._database = database
        self._database.ensure_schema()

    def get_coupon(self, coupon_id: int) -> Coupon:
        with self._database.connect() as connection:
            row = connection.execute(
                "SELECT id, code, discount FROM coupons WHERE id = ?",
                (coupon_id,),
            ).fetchone()

        if row is None:
            raise ValueError(f"Coupon not found: {coupon_id}")

        return Coupon(id=row["id"], code=row["code"], discount=row["discount"])

    def add_coupon(self, coupon: Coupon) -> None:
        with self._database.connect() as connection:
            existing = connection.execute(
                "SELECT 1 FROM coupons WHERE id = ?",
                (coupon.id,),
            ).fetchone()
            if existing is not None:
                raise ValueError(f"Coupon already exists: {coupon.id}")

            connection.execute(
                "INSERT INTO coupons (id, code, discount) VALUES (?, ?, ?)",
                (coupon.id, coupon.code, coupon.discount),
            )

    def update_coupon(self, coupon: Coupon) -> None:
        with self._database.connect() as connection:
            result = connection.execute(
                "UPDATE coupons SET code = ?, discount = ? WHERE id = ?",
                (coupon.code, coupon.discount, coupon.id),
            )

        if result.rowcount == 0:
            raise ValueError(f"Coupon not found: {coupon.id}")

    def delete_coupon(self, coupon_id: int) -> None:
        with self._database.connect() as connection:
            result = connection.execute(
                "DELETE FROM coupons WHERE id = ?",
                (coupon_id,),
            )

        if result.rowcount == 0:
            raise ValueError(f"Coupon not found: {coupon_id}")
