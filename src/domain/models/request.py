from sqlalchemy import Column, String, ForeignKey
from .tenant import Base
import uuid

class Request(Base):
    __tablename__ = "requests"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)