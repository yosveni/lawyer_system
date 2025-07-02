from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...application.services.account_service import AccountService
from ...domain.repositories.account_repository import AccountRepository
from ...application.dtos.account_dto import AccountCreate, AccountResponse
from ...infrastructure.database import get_db
from ...infrastructure.auth.jwt_handler import get_current_user
from ...domain.models.user import User

router = APIRouter()

@router.post("/accounts", response_model=AccountResponse)
async def create_account(account: AccountCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    service = AccountService(AccountRepository(db))
    return service.create_account(account, current_user.tenant_id)

