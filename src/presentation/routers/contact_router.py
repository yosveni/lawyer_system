from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...application.services.contact_service import ContactService
from ...domain.repositories.contact_repository import ContactRepository
from ...application.dtos.contact_dto import ContactCreate, ContactResponse
from ...infrastructure.database import get_db
from ...infrastructure.auth.jwt_handler import get_current_user
from ...domain.models.user import User

router = APIRouter()

@router.post("/contacts", response_model=ContactResponse)
async def create_contact(contact: ContactCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = ContactService(ContactRepository(db))
    return service.create_contact(contact, current_user.tenant_id)