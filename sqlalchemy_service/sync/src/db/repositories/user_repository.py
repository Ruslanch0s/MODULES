from db.database import session_factory
from db.models import UserModel
from db.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[UserModel]):
    def __init__(self):
        super().__init__(model=UserModel)

    def get_by_email(self, email: str) -> UserModel | None:
        print(type(self.model))
        with session_factory() as session:
            return session.query(self.model).filter(
                self.model.email == email
            ).first()
