## app/interfaces/api/endpoints/admin.py
from fastapi import APIRouter
from app.infrastructure.db.memory import db

router = APIRouter()

@router.get("/events")
def list_events():
    return db["events"]