from pydantic import BaseModel

class AccountCreate(BaseModel):
    balance: float

class AccountResponse(BaseModel):
    id: str
    balance: float
    tenant_id: str