from sqlalchemy.orm import Session
from ..models.task import Task
from ...application.dtos.task_dto import TaskCreate

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task: TaskCreate, tenant_id: str) -> Task:
        db_task = Task(**task.dict(), tenant_id=tenant_id)
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task