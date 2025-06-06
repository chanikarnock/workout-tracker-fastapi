from fastapi import HTTPException, status
from app.databases.users_postgres import UsersPostgresRepo
import bcrypt

from app.models.req_model import LoginUserReq


class LoginUserUsecase():
    def __init__(self, user_db_repo: UsersPostgresRepo):
        self.db_repo = user_db_repo
        pass

    def verify_password(self, plain_pwd: str, hashed_pwd: str) -> bool:
        return bcrypt.checkpw(password=plain_pwd.encode('utf-8'), hashed_password=hashed_pwd.encode('utf-8'))

    def execute(self, request_body: LoginUserReq):
        validate_error = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login failed, wrong email or password",
        )

        user_db = self.db_repo.find_user_by_email(email=request_body.email)
        if not user_db:
            print({"message": "No user with this email not found"})
            raise validate_error
        if not self.verify_password(
                plain_pwd=request_body.password, hashed_pwd=user_db.password):
            print({"message": "Login Fail"})
            raise validate_error
        return user_db
