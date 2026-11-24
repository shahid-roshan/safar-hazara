from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Destination, Hotel

app = FastAPI(title="Safar Hazara API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DestinationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    slug: str
    description: str
    latitude: float
    longitude: float
    best_season: str | None = None
    transport: str | None = None
    packing_tips: str | None = None
    local_tips: str | None = None
    image_url: str | None = None


class HotelOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    destination_id: int
    name: str
    description: str | None = None
    price_min: int
    price_max: int
    services: str | None = None
    phone: str | None = None
    image_url: str | None = None


@app.get("/")
def home():
    return {"message": "Safar Hazara chal raha hai"}


@app.get("/destinations", response_model=list[DestinationOut])
def list_destinations(db: Session = Depends(get_db)):
    return db.scalars(select(Destination)).all()


@app.get("/destinations/{slug}", response_model=DestinationOut)
def get_destination(slug: str, db: Session = Depends(get_db)):
    destination = db.scalar(select(Destination).where(Destination.slug == slug))
    if destination is None:
        raise HTTPException(status_code=404, detail="Destination not found")
    return destination


@app.get("/hotels", response_model=list[HotelOut])
def list_hotels(destination_id: int | None = None, db: Session = Depends(get_db)):
    query = select(Hotel)
    if destination_id is not None:
        query = query.where(Hotel.destination_id == destination_id)
    return db.scalars(query).all()


@app.get("/hotels/{hotel_id}", response_model=HotelOut)
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.get(Hotel, hotel_id)
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel