from app.databases.users_postgres import UsersPostgresRepo


class DeleteUserUsecase():
    def __init__(self, user_db_repo: UsersPostgresRepo):
        self.db_repo = user_db_repo
        pass

    def execute(self, user_id: int):
        self.db_repo.delete_user(user_id=user_id)
        return {"message": "Delete success!"} 
