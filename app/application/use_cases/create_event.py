from app.infrastructure.db.database import SessionLocal
from app.infrastructure.db.models import Event

def create_event(title, description, location, date, price, capacity):
    db = SessionLocal()
    try:
        event = Event(
            title=title,
            description=description,
            location=location,
            date=date,
            price=price,
            capacity=capacity
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event.id
    finally:
        db.close()