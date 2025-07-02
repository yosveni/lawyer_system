from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...application.services.activity_service import ActivityService
from ...domain.repositories.activity_repository import ActivityRepository
from ...application.dtos.activity_dto import ActivityCreate, ActivityResponse
from ...infrastructure.database import get_db
from ...infrastructure.auth.jwt_handler import get_current_user
from ...domain.models.user import User

router = APIRouter()

@router.post("/activities", response_model=ActivityResponse)
async def create_activity(activity: ActivityCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = ActivityService(ActivityRepository(db))
    return service.create_activity(activity, current_user.tenant_id)