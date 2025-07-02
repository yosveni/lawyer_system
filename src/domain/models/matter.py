from sqlalchemy import Column, String, ForeignKey
from .tenant import Base
import uuid

class Matter(Base):
    __tablename__ = "matters"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    case_number = Column(String, nullable=False)
    description = Column(String, nullable=False)