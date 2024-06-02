import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_numbers_success():
    response = client.post("/add", json={"batchid": "id0101", "payload": [[1, 2], [3, 4]]})
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == [3, 7]
    assert data["status"] == "complete"

def test_add_numbers_empty_payload():
    response = client.post("/add", json={"batchid": "id0101", "payload": []})
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == []
    assert data["status"] == "complete"

def test_add_numbers_invalid_payload():
    response = client.post("/add", json={"batchid": "id0101", "payload": [[1, "a"], [3, 4]]})
    assert response.status_code == 422  # Unprocessable Entity
