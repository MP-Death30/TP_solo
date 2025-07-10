import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_reservation_failure(monkeypatch):
    # 1. Mock de la fonction reserve_spot utilisée DANS reservations.py
    def mock_reserve_spot(event_id, user_email):
        return False

    # 2. Import après avoir défini le mock
    from app.interfaces.api.endpoints import reservations
    monkeypatch.setattr(reservations, "reserve_spot", mock_reserve_spot)

    # 3. Appel du endpoint
    response = client.post("/reservations/", json={
        "event_id": 999,
        "user_email": "user@example.com"
    })

    # 4. Assertion
    assert response.status_code == 400
    assert response.json()["detail"] == "Reservation failed - Event not found or fully booked"
