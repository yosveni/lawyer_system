import pytest
from fastapi.testclient import TestClient
from ..presentation.main import app

client = TestClient(app)

def test_create_schedule():
    # Requiere autenticación, prueba básica
    response = client.post("/api/schedules", json={"title": "Meeting", "start_time": "2025-07-01T10:00:00", "end_time": "2025-07-01T11:00:00"})
    assert response.status_code == 401  # No autorizado sin token