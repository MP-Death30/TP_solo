## app/application/use_cases/reserve.py
from app.infrastructure.db.memory import db

def reserve_spot(event_id: str, user_email: str):
    for event in db["events"]:
        if event.id == event_id:
            if event.reservations < event.capacity:
                event.reservations += 1
                db["reservations"].append({"event_id": event_id, "user_email": user_email})
                return True
    return False