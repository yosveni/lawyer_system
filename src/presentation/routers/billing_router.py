from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...application.services.billing_service import BillingService
from ...domain.repositories.billing_repository import BillingRepository
from ...application.dtos.billing_dto import BillingCreate, BillingResponse
from ...infrastructure.database import get_db
from ...infrastructure.auth.jwt_handler import get_current_user
from ...domain.models.user import User

router = APIRouter()

@router.post("/billings", response_model=BillingResponse)
async def create_billing(billing: BillingCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = BillingService(BillingRepository(db))
    return service.create_billing(billing, current_user.tenant_id)