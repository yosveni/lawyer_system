from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...application.services.request_service import RequestService
from ...domain.repositories.request_repository import RequestRepository
from ...application.dtos.request_dto import RequestCreate, RequestResponse
from ...infrastructure.database import get_db
from ...infrastructure.auth.jwt_handler import get_current_user
from ...domain.models.user import User

router = APIRouter()

@router.post("/requests", response_model=RequestResponse)
async def create_request(request: RequestCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = RequestService(RequestRepository(db))
    return service.create_request(request, current_user.tenant_id)