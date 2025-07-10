# ===== app/interfaces/api/endpoints/reservations.py =====
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.application.use_cases.reserve import reserve_spot

router = APIRouter()

class ReserveRequest(BaseModel):
    event_id: int
    user_email: str

@router.post("/")
def reserve_endpoint(request: ReserveRequest):
    try:
        success = reserve_spot(request.event_id, request.user_email)
        if not success:
            raise HTTPException(status_code=400, detail="Reservation failed - Event not found or fully booked")
        return {"message": "Reservation successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making reservation: {str(e)}")
