from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...application.services.task_service import TaskService
from ...domain.repositories.task_repository import TaskRepository
from ...application.dtos.task_dto import TaskCreate, TaskResponse
from ...infrastructure.database import get_db
from ...infrastructure.auth.jwt_handler import get_current_user
from ...domain.models.user import User

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = TaskService(TaskRepository(db))
    return service.create_task(task, current_user.tenant_id)