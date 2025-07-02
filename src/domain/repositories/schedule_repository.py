from sqlalchemy.orm import Session
from ..models.schedule import Schedule
from ...application.dtos.schedule_dto import ScheduleCreate

class ScheduleRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_schedule(self, schedule: ScheduleCreate, tenant_id: str) -> Schedule:
        db_schedule = Schedule(**schedule.dict(), tenant_id=tenant_id)
        self.db.add(db_schedule)
        self.db.commit()
        self.db.refresh(db_schedule)
        return db_schedule