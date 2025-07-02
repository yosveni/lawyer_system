from sqlalchemy.orm import Session
from ..models.account import Account
from ...application.dtos.account_dto import AccountCreate

class AccountRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_account(self, account: AccountCreate, tenant_id: str) -> Account:
        db_account = Account(**account.dict(), tenant_id=tenant_id)
        self.db.add(db_account)
        self.db.commit()
        self.db.refresh(db_account)
        return db_account