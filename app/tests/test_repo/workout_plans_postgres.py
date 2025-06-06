# tests/test_router.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_all_workout_success():
    return