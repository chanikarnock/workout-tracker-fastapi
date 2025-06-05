from app.databases.users_postgres import UsersPostgresRepo
import bcrypt


class GetUserUsecase():
    def __init__(self, user_db_repo: UsersPostgresRepo):
        self.db_repo = user_db_repo
        pass

    def execute(self, email: str):
        return self.db_repo.find_user_by_email(email=email)
