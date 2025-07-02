from sqlalchemy import Column, String, DateTime, ForeignKey
from .tenant import Base
import uuid

class Activity(Base):
    __tablename__ = "activities"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    description = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)