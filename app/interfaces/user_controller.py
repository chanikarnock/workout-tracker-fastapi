from app.databases.users_postgres import UsersPostgresRepo
from app.usecases.user.get_user_use_case import GetUserUsecase
from app.usecases.user.login_use_case import LoginUserUsecase
from app.usecases.user.register_user_use_case import RegisterUserUsecase
from app.usecases.user.update_user_use_case import UpdateUserUsecase
from app.usecases.user.delete_user_use_case import DeleteUserUsecase


class UserController():
    def __init__(self):
        self.user_db = UsersPostgresRepo()

    def get_user(self, email: str):
        return GetUserUsecase(user_db_repo=self.user_db).execute(email=email)

    def register_user(self, request_body: dict):
        result = RegisterUserUsecase(user_db_repo=self.user_db).execute(
            request_body=request_body)
        return result

    def login_user(self, request_body: dict):
        result = LoginUserUsecase(user_db_repo=self.user_db).execute(
            request_body=request_body)
        return result

    def update_user(self, user_id: int, request_body: dict):
        result = UpdateUserUsecase(user_db_repo=self.user_db).execute(user_id=user_id,
            request_body=request_body)
        return result
    
    def delete_user(self, user_id: int):
        result = DeleteUserUsecase(user_db_repo=self.user_db).execute(user_id=user_id)
        return result
