# ===== app/application/use_cases/get_events.py =====
from app.infrastructure.db.database import SessionLocal
from app.infrastructure.db.models import Event
from typing import List

def get_all_events() -> List[Event]:
    db = SessionLocal()
    try:
        events = db.query(Event).all()
        return events
    finally:
        db.close()

def get_event_by_id(event_id: int) -> Event:
    db = SessionLocal()
    try:
        event = db.query(Event).filter(Event.id == event_id).first()
        if not event:
            raise ValueError(f"Event with id {event_id} not found")
        return event
    finally:
        db.close()