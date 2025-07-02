from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...application.services.schedule_service import ScheduleService
from ...domain.repositories.schedule_repository import ScheduleRepository
from ...application.dtos.schedule_dto import ScheduleCreate, ScheduleResponse
from ...infrastructure.database import get_db
from ...infrastructure.auth.jwt_handler import get_current_user
from ...domain.models.user import User

router = APIRouter()

@router.post("/schedules", response_model=ScheduleResponse)
async def create_schedule(schedule: ScheduleCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = ScheduleService(ScheduleRepository(db))
    return service.create_schedule(schedule, current_user.tenant_id)