from sqlalchemy.orm import Session
from ...domain.models.tenant import Tenant

class TenantRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, tenant: Tenant) -> Tenant:
        """Create a new tenant in the database."""
        self.db.add(tenant)
        self.db.commit()
        self.db.refresh(tenant)
        return tenant

    def get_by_id(self, tenant_id: str) -> Tenant | None:
        """Retrieve a tenant by its ID."""
        return self.db.query(Tenant).filter(Tenant.id == tenant_id).first()

    def get_all(self) -> list[Tenant]:
        """Retrieve all tenants."""
        return self.db.query(Tenant).all()