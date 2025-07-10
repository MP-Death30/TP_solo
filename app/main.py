# ===== app/main.py =====
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.interfaces.api.routes import router
from app.infrastructure.db.database import engine
from app.infrastructure.db.models import Base
import os

# Créer les tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Event Booking App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

# Serve frontend
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
def read_index():
    frontend_file = os.path.join(frontend_path, "index.html")
    if os.path.exists(frontend_file):
        return FileResponse(frontend_file)
    return {"message": "Event Booking API is running", "endpoints": ["/events", "/reservations", "/admin"]}

@app.get("/organisateur")
def read_organisateur():
    frontend_file = os.path.join(frontend_path, "organisateur.html")
    if os.path.exists(frontend_file):
        return FileResponse(frontend_file)
    return {"message": "Organisateur page not found"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "MariaDB Galera Cluster"}