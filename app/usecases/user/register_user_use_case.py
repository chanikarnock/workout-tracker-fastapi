from app.databases.users_postgres import UsersPostgresRepo
import bcrypt

from app.models.req_model import RegisterUserReq


class RegisterUserUsecase():
    def __init__(self, user_db_repo: UsersPostgresRepo) -> None:
        self.db_repo = user_db_repo

    def verify_password(plain_pwd, hashed_pwd):
        return bcrypt.checkpw(password=plain_pwd, hashed_password=hashed_pwd)

    def hash_password(self, pwd: str):
        hashed_pwd = bcrypt.hashpw(password=pwd.encode('utf-8'), salt=bcrypt.gensalt())
        return hashed_pwd.decode('utf-8')

    def execute(self, request_body: RegisterUserReq):
        is_email_existed = self.db_repo.find_user_by_email(
            email=request_body.email)
        if is_email_existed:
            return {"message": "User with this email already existed!"}
        self.db_repo.create_new_user(first_name=request_body.first_name,
                                     last_name=request_body.last_name,
                                     email=request_body.email,
                                     pwd=self.hash_password(pwd=request_body.password))
        return {"message": "create new user success!"}
