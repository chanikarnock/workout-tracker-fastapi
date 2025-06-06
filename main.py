from fastapi import FastAPI
from app.routers.root_router import app as root_router

app = FastAPI()

app.mount("/workout-tracker", root_router)
