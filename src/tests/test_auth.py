import pytest
from fastapi.testclient import TestClient
from ..presentation.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/auth/users", json={"email": "test@example.com", "password": "password123", "tenant_id": "test-tenant"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"