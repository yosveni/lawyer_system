from sqlalchemy.orm import Session
from ..models.activity import Activity
from ...application.dtos.activity_dto import ActivityCreate

class ActivityRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_activity(self, activity: ActivityCreate, tenant_id: str) -> Activity:
        db_activity = Activity(**activity.dict(), tenant_id=tenant_id)
        self.db.add(db_activity)
        self.db.commit()
        self.db.refresh(db_activity)
        return db_activity