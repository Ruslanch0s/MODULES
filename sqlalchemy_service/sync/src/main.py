import time

from db.schemas import UserCreateSchema
from dependencies import user_service


def background_task():
    while True:
        # Пример создания пользователя
        new_user = UserCreateSchema(name="Background User",
                                    email="background@exadmple.com",
                                    hashed_password="background")

        user = user_service.create_user(new_user)
        print(f"Created user: {user.name} with email {user.email}")

        # Пример чтения пользователя
        user = user_service.get_user(user.id)
        if user:
            print(f"Read user: {user.name} with email {user.email}")

        # Интервал выполнения задачи
        time.sleep(60)  # Выполнять задачу каждую минуту


background_task()
