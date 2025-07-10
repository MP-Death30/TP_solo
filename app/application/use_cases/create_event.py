# ===== app/application/use_cases/create_event.py =====
from app.infrastructure.db.database import SessionLocal
from app.infrastructure.db.models import Event

def create_event(title: str, description: str, location: str, date: str, price: float, capacity: int) -> int:
    db = SessionLocal()
    try:
        event = Event(
            title=title,
            description=description,
            location=location,
            date=date,
            price=price,
            capacity=capacity,
            reservations=0
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event.id
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()