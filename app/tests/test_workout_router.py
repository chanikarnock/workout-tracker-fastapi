import pytest
from fastapi.testclient import TestClient
from main import app
from datetime import timedelta

client = TestClient(app)

create_plan_req_body = {
    "name": "My New Test Plan",
    "description": "test plan",
    "start_at": "2025-06-01T10:00:00",
    "stop_at": "2025-06-01T11:00:00",
    "exercise_list": [
            {
                "exec_id": 3
            }
    ]
}


def test_create_workout_plan_fail_no_header(auth_token):
    request_body = create_plan_req_body
    response = client.post("/workout-tracker/workout/", json=request_body)
    assert response.status_code == 401


def test_create_workout_plan_fail_no_req_body(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/workout-tracker/workout/", headers=headers)
    assert response.status_code == 422


def test_create_workout_plan_fail_missing_field_req_body(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    request_body = {
        "description": "test plan",
        "start_at": "2025-06-01T10:00:00",
        "exercise_list": [
            {
                "exec_id": 3
            }
        ]
    }
    response = client.post("/workout-tracker/workout/",
                           headers=headers, json=request_body)
    assert response.status_code == 422


def test_create_workout_plan_success(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    request_body = create_plan_req_body
    response = client.post("/workout-tracker/workout/",
                           headers=headers, json=request_body)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == request_body.get("name")
    assert data["description"] == request_body.get("description")

# python -m pytest app/tests/test_workout_router.py