from sqlalchemy import create_engine
import sqlalchemy.exc
from sqlalchemy.orm import sessionmaker
from settings import PG_DB_HOST, PG_DB_NAME, PG_DB_PASS, PG_DB_PORT, PG_DB_USER

from app.models import users, workout_plans, exercises
from app.models.base import Base

class PostgresRepo:
    def __init__(
        self,
        db_type: str = "postgresql+psycopg2",
        db_host: str = PG_DB_HOST,
        db_port: str = PG_DB_PORT,
        db_username: str = PG_DB_USER,
        db_password: str = PG_DB_PASS,
        db_name: str = PG_DB_NAME
    ):
        self._engine = create_engine(
            f"{db_type}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")
        self.SessionLocal = sessionmaker(autoflush=False, bind=self._engine)

    def check_connection(self):
        con_status = True
        try:
            conn = self._engine.connect()
            conn.close()
        except sqlalchemy.exc.OperationalError as e:
            con_status = False
        return con_status

    def create_tables(self) -> None:
        Base.metadata.create_all(bind=self._engine)

        


if __name__ == '__main__':
    db_repo = PostgresRepo(
        db_type='postgresql+psycopg2',
        db_host=PG_DB_HOST,
        db_port=PG_DB_PORT,
        db_username=PG_DB_USER,
        db_password=PG_DB_PASS,
        db_name=PG_DB_NAME,
    )
    db_repo.create_tables()
