import pytest
from fastapi.testclient import TestClient
from main import app
from datetime import timedelta

client = TestClient(app)

test_user = {
    "email": "testuser@example.com",
    "password": "test1234",
    "first_name": "Test User",
    "last_name": "Test User"
}

test_user_missing_email = {
    "password": "test1234",
    "first_name": "Test User",
    "last_name": "Test User"
}


def test_register_user_fail_missing_request_body():
    response = client.post("/workout-tracker/user/register")
    assert response.status_code == 422


def test_register_user_fail_missing_email():
    response = client.post("/workout-tracker/user/register",
                           json=test_user_missing_email)
    assert response.status_code == 422


def test_register_user_success():
    response = client.post("/workout-tracker/user/register", json=test_user)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data


def test_login_user_fail_missing_email():
    response = client.post("/workout-tracker/user/login", json={
        "password": test_user["password"]
    })
    assert response.status_code == 422


def test_login_user_fail_wrong_password():
    response = client.post("/workout-tracker/user/login", json={
        "email": test_user["email"],
        "password": "wrongpwd"
    })
    assert response.status_code == 401


def test_login_user_success():
    response = client.post("/workout-tracker/user/login", json={
        "email": test_user["email"],
        "password": test_user["password"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    global AUTH_TOKEN
    AUTH_TOKEN = data["access_token"]


def test_update_user_fail_empty_string():
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    response = client.post("/workout-tracker/user/update", json={
        "first_name": ""
    }, headers=headers)
    assert response.status_code == 422


def test_update_user_fail_no_header():
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    response = client.post("/workout-tracker/user/update")
    assert response.status_code == 401
    

def test_update_user_fail_wrong_header():
    headers = {"Authorization": f"Bearer mock"}
    response = client.post("/workout-tracker/user/update")
    assert response.status_code == 401
    
        
def test_update_user_fail_no_req_body():
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    response = client.post("/workout-tracker/user/update", headers=headers)
    assert response.status_code == 422


def test_update_user_success():
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    response = client.post("/workout-tracker/user/update", json={
        "first_name": "Updated Name"
    }, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Update success!"}


def test_delete_user_success():
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    response = client.delete("/workout-tracker/user/delete", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Delete success!"}
