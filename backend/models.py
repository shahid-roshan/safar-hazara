from datetime import datetime
from sqlalchemy import String, Text, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Destination(Base):
    __tablename__ = "destinations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    slug: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(Text)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    best_season: Mapped[str | None] = mapped_column(String(100))
    transport: Mapped[str | None] = mapped_column(Text)
    packing_tips: Mapped[str | None] = mapped_column(Text)
    local_tips: Mapped[str | None] = mapped_column(Text)
    image_url: Mapped[str | None] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())