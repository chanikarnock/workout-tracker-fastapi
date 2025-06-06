from app.databases.users_postgres import UsersPostgresRepo
import bcrypt


class UpdateUserUsecase():
    def __init__(self, user_db_repo: UsersPostgresRepo):
        self.db_repo = user_db_repo
        pass

    def execute(self, user_id: int, request_body: dict):
        self.db_repo.update_user(user_id=user_id, request_body=dict(request_body))
        return {"message": "Update success!"}
