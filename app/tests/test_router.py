# tests/test_router.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_server_status():
    response = client.get("/workout-tracker/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
