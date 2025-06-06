# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def auth_token():
    register_data = {
        "email": "testuser@example.com",
        "password": "test1234",
        "first_name": "Test",
        "last_name": "User"
    }

    client.post("/workout-tracker/user/register", json=register_data)

    login_data = {
        "email": "testuser@example.com",
        "password": "test1234"
    }

    response = client.post("/workout-tracker/user/login", json=login_data)
    assert response.status_code == 200, f"Login failed: {response.json()}"
    return response.json()["access_token"]

@pytest.fixture
def auth_headers(auth_token):
    return {
        "Authorization": f"Bearer {auth_token}"
    }
