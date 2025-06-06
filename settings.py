import logging
import os
from pathlib import Path

import pytz
from dotenv import load_dotenv

PG_DB_HOST = os.getenv("PG_DB_HOST")
PG_DB_NAME = os.getenv("PG_DB_NAME")
PG_DB_PASS = os.getenv("PG_DB_PASS")
PG_DB_PORT = os.getenv("PG_DB_PORT")
PG_DB_USER = os.getenv("PG_DB_USER")

SECRET_KEY = os.getenv("SECRET_KEY")
HASH_ALGO = os.getenv("HASH_ALGO")
TOKEN_EXPIRE_MIN = os.getenv("TOKEN_EXPIRE_MIN")