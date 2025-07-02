from sqlalchemy.orm import Session
from ..models.matter import Matter
from ...application.dtos.matter_dto import MatterCreate

class MatterRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_matter(self, matter: MatterCreate, tenant_id: str) -> Matter:
        db_matter = Matter(**matter.dict(), tenant_id=tenant_id)
        self.db.add(db_matter)
        self.db.commit()
        self.db.refresh(db_matter)
        return db_matter