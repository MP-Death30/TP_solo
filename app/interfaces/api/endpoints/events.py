# ===== app/interfaces/api/endpoints/events.py =====
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.application.use_cases.create_event import create_event
from app.application.use_cases.get_events import get_all_events, get_event_by_id

router = APIRouter()

class EventCreateRequest(BaseModel):
    title: str
    description: str
    location: str
    date: str
    price: float
    capacity: int

class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    location: str
    date: str
    price: float
    capacity: int
    reservations: int
    
    class Config:
        from_attributes = True

@router.post("/", response_model=dict)
def create_event_endpoint(request: EventCreateRequest):
    try:
        event_id = create_event(
            title=request.title,
            description=request.description,
            location=request.location,
            date=request.date,
            price=request.price,
            capacity=request.capacity
        )
        return {"id": event_id, "message": "Event created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating event: {str(e)}")

@router.get("/", response_model=List[EventResponse])
def list_events():
    try:
        events = get_all_events()
        return events
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving events: {str(e)}")

@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int):
    try:
        event = get_event_by_id(event_id)
        return event
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving event: {str(e)}")
