from ...domain.repositories.billing_repository import BillingRepository
from ...application.dtos.billing_dto import BillingCreate, BillingResponse

class BillingService:
    def __init__(self, repo: BillingRepository):
        self.repo = repo

    def create_billing(self, billing: BillingCreate, tenant_id: str) -> BillingResponse:
        db_billing = self.repo.create_billing(billing, tenant_id)
        return BillingResponse(**db_billing.__dict__)