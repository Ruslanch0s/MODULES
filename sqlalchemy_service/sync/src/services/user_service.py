from db.models import UserModel
from db.repositories.user_repository import UserRepository
from db.schemas import UserCreateSchema


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_create: UserCreateSchema) -> UserModel:
        existing_user = self.user_repository.get_by_email(
            user_create.email)
        if existing_user:
            raise ValueError("User with this email already exists.")
        new_user = UserModel(**user_create.model_dump())
        return self.user_repository.create(new_user)

    def get_user(self, user_id: int) -> UserModel:
        user = self.user_repository.get(user_id)
        if not user:
            raise ValueError("User not found.")
        return user
