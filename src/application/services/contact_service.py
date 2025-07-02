from ...domain.repositories.contact_repository import ContactRepository
from ...application.dtos.contact_dto import ContactCreate, ContactResponse

class ContactService:
    def __init__(self, repo: ContactRepository):
        self.repo = repo

    def create_contact(self, contact: ContactCreate, tenant_id: str) -> ContactResponse:
        db_contact = self.repo.create_contact(contact, tenant_id)
        return ContactResponse(**db_contact.__dict__)