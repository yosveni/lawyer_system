from pydantic import BaseModel
from datetime import datetime

class PaymentCreate(BaseModel):
    amount: float
    payment_date: datetime

class PaymentResponse(BaseModel):
    id: str
    amount: float
    payment_date: datetime
    tenant_id: str