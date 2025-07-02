from pydantic import BaseModel

class BillingCreate(BaseModel):
    amount: float
    description: str

class BillingResponse(BaseModel):
    id: str
    amount: float
    description: str
    tenant_id: str