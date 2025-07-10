from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000))
    location = Column(String(255))
    date = Column(String(50))  # ou DateTime si vous voulez un vrai datetime
    price = Column(Float)
    capacity = Column(Integer)