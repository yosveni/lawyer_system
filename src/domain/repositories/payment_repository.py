from sqlalchemy.orm import Session
from ..models.payment import Payment
from ...application.dtos.payment_dto import PaymentCreate

class PaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_payment(self, payment: PaymentCreate, tenant_id: str) -> Payment:
        db_payment = Payment(**payment.dict(), tenant_id=tenant_id)
        self.db.add(db_payment)
        self.db.commit()
        self.db.refresh(db_payment)
        return db_payment