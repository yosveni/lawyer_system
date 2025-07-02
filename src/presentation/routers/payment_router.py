from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...application.services.payment_service import PaymentService
from ...domain.repositories.payment_repository import PaymentRepository
from ...application.dtos.payment_dto import PaymentCreate, PaymentResponse
from ...infrastructure.database import get_db
from ...infrastructure.auth.jwt_handler import get_current_user
from ...domain.models.user import User

router = APIRouter()

@router.post("/payments", response_model=PaymentResponse)
async def create_payment(payment: PaymentCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = PaymentService(PaymentRepository(db))
    return service.create_payment(payment, current_user.tenant_id)