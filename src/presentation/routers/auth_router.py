from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ...application.services.auth_service import AuthService
from ...application.dtos.user_dto import UserCreate, UserResponse
from ...application.dtos.tenant_dto import TenantCreate, TenantResponse
from ...infrastructure.database import get_db
from ...infrastructure.auth.jwt_handler import create_access_token

router = APIRouter(tags=["Authentication", "Tenants"])

@router.post("/tenants", response_model=TenantResponse, status_code=status.HTTP_201_CREATED, tags=["auth"])
def create_tenant(tenant: TenantCreate, db: Session = Depends(get_db)):
    """Create a new tenant."""
    auth_service = AuthService(db)
    try:
        return auth_service.create_tenant(tenant)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["auth"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    auth_service = AuthService(db)
    try:
        return auth_service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/token", tags=["auth"])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Generate a JWT token for a user."""
    auth_service = AuthService(db)
    print()
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}