## event_booking_app/app/interfaces/api/routes.py
from fastapi import APIRouter
from app.interfaces.api.endpoints import events, reservations, admin

router = APIRouter()
router.include_router(events.router, prefix="/events", tags=["Events"])
router.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])
router.include_router(admin.router, prefix="/admin", tags=["Admin"])