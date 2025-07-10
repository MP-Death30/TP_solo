from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.application.use_cases.create_event import create_event
from app.infrastructure.db.database import SessionLocal
from app.infrastructure.db.models import Event

router = APIRouter()

class EventCreateRequest(BaseModel):
    title: str
    description: str
    location: str
    date: str
    price: float
    capacity: int

@router.post("/")
def create_event_endpoint(request: EventCreateRequest):
    event_id = create_event(
        title=request.title,
        description=request.description,
        location=request.location,
        date=request.date,
        price=request.price,
        capacity=request.capacity
    )
    return {"id": event_id, "message": "Event created"}

@router.get("/")
def list_events():
    events = get_all_events()  # use case à créer
    return events