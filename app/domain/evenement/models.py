from dataclasses import dataclass

@dataclass
class Event:
    id: str
    title: str
    description: str
    location: str
    date: str
    price: float
    capacity: int
    reservations: int = 0