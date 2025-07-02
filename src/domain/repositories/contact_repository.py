from sqlalchemy.orm import Session
from ..models.contact import Contact
from ...application.dtos.contact_dto import ContactCreate

class ContactRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_contact(self, contact: ContactCreate, tenant_id: str) -> Contact:
        db_contact = Contact(**contact.dict(), tenant_id=tenant_id)
        self.db.add(db_contact)
        self.db.commit()
        self.db.refresh(db_contact)
        return db_contact