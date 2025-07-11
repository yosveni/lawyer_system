from sqlalchemy.orm import Session
from ...domain.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        """Create a new user in the database."""
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str) -> User | None:
        """Retrieve a user by email."""
        return self.db.query(User).filter(User.email == email).first()

    def get_by_id(self, user_id: str) -> User | None:
        """Retrieve a user by ID."""
        return self.db.query(User).filter(User.id == user_id).first()

    def get_all(self) -> list[User]:
        """Retrieve all users."""
        return self.db.query(User).all()