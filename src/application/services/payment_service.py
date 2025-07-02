from ...domain.repositories.payment_repository import PaymentRepository
from ...application.dtos.payment_dto import PaymentCreate, PaymentResponse

class PaymentService:
    def __init__(self, repo: PaymentRepository):
        self.repo = repo

    def create_payment(self, payment: PaymentCreate, tenant_id: str) -> PaymentResponse:
        db_payment = self.repo.create_payment(payment, tenant_id)
        return PaymentResponse(**db_payment.__dict__)