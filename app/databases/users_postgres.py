from fastapi import HTTPException, status
from app.databases.postgres import PostgresRepo
from app.models.users import User
from settings import PG_DB_HOST, PG_DB_NAME, PG_DB_PASS, PG_DB_PORT, PG_DB_USER


class UsersPostgresRepo(PostgresRepo):
    def __init__(self,):
        super().__init__(
            db_type='postgresql+psycopg2',
            db_host=PG_DB_HOST,
            db_port=PG_DB_PORT,
            db_username=PG_DB_USER,
            db_password=PG_DB_PASS,
            db_name=PG_DB_NAME,
        )

    def find_user_by_email(
        self,
        email: str,
    ):
        with self.SessionLocal() as s:
            return s.query(User).filter_by(email=email).first()

    def create_new_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
        pwd: str
    ):
        new_user = User(first_name=first_name,
                        last_name=last_name, email=email, password=pwd)
        with self.SessionLocal() as s:
            s.add(new_user)
            s.commit()
        return

    def update_user(
        self,
        user_id: int,
        request_body: dict
    ):
        with self.SessionLocal() as s:
            target_user = s.query(User).filter_by(id=user_id).first()
            if not target_user:
                raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=str("User plan not found")
            )
            for key, value in request_body.items():
                if value is not None and hasattr(target_user, key):
                    setattr(target_user, key, value)
            s.commit()
            s.refresh(target_user)
        return target_user

    def delete_user(
        self,
        user_id: int,
    ):
        with self.SessionLocal() as s:
            target_user = s.query(User).filter_by(id=user_id).first()
            if not target_user:
                raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=str("User plan not found")
            )
            s.delete(target_user)
            s.commit()
        return


if __name__ == '__main__':
    # python -m app.databases.user_postgres
    db_repo = UsersPostgresRepo(
        db_host=PG_DB_HOST,
        db_port=PG_DB_PORT,
        db_username=PG_DB_USER,
        db_password=PG_DB_PASS,
        db_name=PG_DB_NAME,
    )
    result = db_repo.find_user_by_email(email="testxxx@gmail.com")
    print(f"==>> result: {result}")
