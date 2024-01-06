from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_execute_r_code_success():
    response = client.post("/execute-r", json={"code": "print('Hello, R!')"})
    assert response.status_code == 200
    assert response.json() == {"message": "R code executed successfully"}


def test_execute_r_code_failure():
    response = client.post("/execute-r", json={"code": "invalid R code"})
    assert response.status_code == 400
    assert response.json().get("detail") == "Invalid R code"
