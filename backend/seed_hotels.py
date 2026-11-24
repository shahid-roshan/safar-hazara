from sqlalchemy import select
from database import SessionLocal
from models import Destination, Hotel

# NOTE: yeh sample/placeholder data hai, asli hotels ki research baad mein karenge.
hotels_data = [
    dict(
        destination_slug="shogran",
        name="Shogran Valley Guest House (sample)",
        description="Sample hotel: Shogran mein sasta guest house.",
        price_min=3000,
        price_max=5000,
        services="Nashta, garam paani, parking",
    ),
    dict(
        destination_slug="shogran",
        name="Siri Paye Resort (sample)",
        description="Sample hotel: Shogran mein behtar resort.",
        price_min=8000,
        price_max=15000,
        services="Nashta, garam paani, parking, view point",
    ),
    dict(
        destination_slug="nathia-gali",
        name="Nathia Gali Lodge (sample)",
        description="Sample hotel: Nathia Gali mein jungle ke qareeb lodge.",
        price_min=4000,
        price_max=7000,
        services="Nashta, garam paani, bonfire",
    ),
]

with SessionLocal() as db:
    for data in hotels_data:
        data = dict(data)
        slug = data.pop("destination_slug")

        destination = db.scalar(select(Destination).where(Destination.slug == slug))
        if destination is None:
            print("destination nahi mili:", slug)
            continue

        exists = db.scalar(
            select(Hotel).where(
                Hotel.destination_id == destination.id,
                Hotel.name == data["name"],
            )
        )
        if exists:
            print("skip:", data["name"])
            continue

        db.add(Hotel(destination_id=destination.id, **data))
        print("added:", data["name"])
    db.commit()