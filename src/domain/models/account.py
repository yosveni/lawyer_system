from sqlalchemy import Column, String, Float, ForeignKey
from .tenant import Base
import uuid

class Account(Base):
    __tablename__ = "accounts"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    balance = Column(Float, nullable=False)