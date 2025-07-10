# ===== app/application/use_cases/reserve.py =====
from app.infrastructure.db.database import SessionLocal
from app.infrastructure.db.models import Event

def reserve_spot(event_id: int, user_email: str) -> bool:
    db = SessionLocal()
    try:
        event = db.query(Event).filter(Event.id == event_id).first()
        if not event:
            return False
        
        if event.reservations < event.capacity:
            event.reservations += 1
            db.commit()
            return True
        return False
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()