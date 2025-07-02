from ...domain.repositories.account_repository import AccountRepository
from ...application.dtos.account_dto import AccountCreate, AccountResponse

class AccountService:
    def __init__(self, repo: AccountRepository):
        self.repo = repo

    def create_account(self, account: AccountCreate, tenant_id: str) -> AccountResponse:
        db_account = self.repo.create_account(account, tenant_id)
        return AccountResponse(**db_account.__dict__)