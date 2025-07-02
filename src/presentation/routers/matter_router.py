from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...application.services.matter_service import MatterService
from ...domain.repositories.matter_repository import MatterRepository
from ...application.dtos.matter_dto import MatterCreate, MatterResponse
from ...infrastructure.database import get_db
from ...infrastructure.auth.jwt_handler import get_current_user
from ...domain.models.user import User

router = APIRouter()

@router.post("/matters", response_model=MatterResponse)
async def create_matter(matter: MatterCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = MatterService(MatterRepository(db))
    return service.create_matter(matter, current_user.tenant_id)