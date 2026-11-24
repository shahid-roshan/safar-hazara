from sqlalchemy import select
from database import SessionLocal
from models import Destination

new_places = [
    dict(
        name="Shogran",
        slug="shogran",
        description="Shogran Kaghan Valley ka khoobsurat hill station hai.",
        latitude=34.62,
        longitude=73.47,
        best_season="May se September",
        transport="Naran ya Kaghan se jeep ka safar.",
        packing_tips="Garam kapre aur achay joote.",
        local_tips="Mausam jaldi badal jata hai, pehle check kar lein.",
    ),
    dict(
        name="Nathia Gali",
        slug="nathia-gali",
        description="Nathia Gali Galiyat ka jungle wala hill station hai.",
        latitude=34.07,
        longitude=73.38,
        best_season="April se October",
        transport="Abbottabad se road ka safar.",
        packing_tips="Halka garam kapra aur chhatri.",
        local_tips="Weekend par rush hota hai, hafte ke din behtar hain.",
    ),
]

with SessionLocal() as db:
    for data in new_places:
        exists = db.scalar(select(Destination).where(Destination.slug == data["slug"]))
        if exists:
            print("skip:", data["name"])
            continue
        db.add(Destination(**data))
        print("added:", data["name"])
    db.commit()