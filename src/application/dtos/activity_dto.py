from pydantic import BaseModel
from datetime import datetime

class ActivityCreate(BaseModel):
    description: str
    timestamp: datetime

class ActivityResponse(BaseModel):
    id: str
    description: str
    timestamp: datetime
    tenant_id: str