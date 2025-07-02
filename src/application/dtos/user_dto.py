from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    tenant_id: UUID

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    tenant_id: UUID