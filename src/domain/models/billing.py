from sqlalchemy import Column, String, Float, ForeignKey
from .tenant import Base
import uuid

class Billing(Base):
    __tablename__ = "billings"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)