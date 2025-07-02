from sqlalchemy.orm import Session
from ..models.billing import Billing
from ...application.dtos.billing_dto import BillingCreate

class BillingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_billing(self, billing: BillingCreate, tenant_id: str) -> Billing:
        db_billing = Billing(**billing.dict(), tenant_id=tenant_id)
        self.db.add(db_billing)
        self.db.commit()
        self.db.refresh(db_billing)
        return db_billing