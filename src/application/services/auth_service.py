from sqlalchemy.orm import Session
from ...domain.models.user import User
from ...domain.models.tenant import Tenant
from ...domain.repositories.user_repository import UserRepository
from ...domain.repositories.tenant_repository import TenantRepository
from ...application.dtos.user_dto import UserCreate, UserResponse
from ...application.dtos.tenant_dto import TenantCreate, TenantResponse
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self,  db: Session):
        self.db = db
        self.user_repository = UserRepository(db)
        self.tenant_repository = TenantRepository(db)
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)

    def authenticate_user(self, email: str, password: str) -> User:
        user = self.user_repository.get_user_by_email(email)
        if not user or not self.verify_password(password, user.password_hash):
            return None
        return user

    def create_user(self, user: User) -> User:
        """Create a new user."""
        hashed_password = self.pwd_context.hash(user.password_hash)
        db_user = User(email=user.email, password_hash=hashed_password, tenant_id=user.tenant_id)
        created_user = self.user_repository.create(db_user)
        return UserResponse(id=created_user.id, email=created_user.email, tenant_id=created_user.tenant_id)

    def create_tenant(self, tenant: TenantCreate) -> TenantResponse:
        """Create a new tenant."""
        db_tenant = Tenant(name=tenant.name)
        created_tenant = self.tenant_repository.create(db_tenant)
        return TenantResponse(id=created_tenant.id, name=created_tenant.name)

    def authenticate_user(self, email: str, password: str) -> User:
        """Authenticate a user by email and password."""
        user = self.user_repository.get_user_by_email(email)
        if not user or not self.pwd_context.verify(password, user.password_hash):
            return None
        return user