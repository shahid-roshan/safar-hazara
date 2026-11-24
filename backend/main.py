from fastapi import FastAPI, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Destination

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


@app.get("/")
def home():
    return {"message": "Safar Hazara chal raha hai"}


@app.get("/destinations", response_model=list[DestinationOut])
def list_destinations(db: Session = Depends(get_db)):
    return db.scalars(select(Destination)).all()