from pydantic import BaseModel
from datetime import datetime

class ScheduleCreate(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime

class ScheduleResponse(BaseModel):
    id: str
    title: str
    start_time: datetime
    end_time: datetime
    tenant_id: str