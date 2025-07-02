from pydantic import BaseModel
from uuid import UUID

class TenantCreate(BaseModel):
    name: str

class TenantResponse(BaseModel):
    id: UUID
    name: str