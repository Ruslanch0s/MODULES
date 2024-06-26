from db.repositories.user_repository import UserRepository
from services.user_service import UserService

user_repository = UserRepository()
user_service = UserService(user_repository=user_repository)
