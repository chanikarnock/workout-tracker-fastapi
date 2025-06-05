from fastapi import FastAPI
from app.routers.user_router import user_router
from app.routers.workout_router import workout_router

app = FastAPI()

@app.get("/")
def server_status():
    return {"message": "Hello World"}

app.include_router(router=user_router, prefix="/user")
app.include_router(router=workout_router, prefix="/workout")