# ===== app/interfaces/api/endpoints/admin.py =====
from fastapi import APIRouter
from app.application.use_cases.get_events import get_all_events

router = APIRouter()

@router.get("/events")
def admin_list_events():
    try:
        events = get_all_events()
        return events
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving events: {str(e)}")
