from database import SessionLocal
from models import Destination

with SessionLocal() as db:
    naran = Destination(
        name="Naran",
        slug="naran",
        description="Naran Kaghan Valley ka mashhoor qasba hai.",
        latitude=34.9026,
        longitude=73.6505,
        best_season="June se September",
        transport="Mansehra se Naran tak road ka safar.",
        packing_tips="Garam kapre aur barsaati.",
        local_tips="Subah jaldi nikalna behtar hai.",
    )
    db.add(naran)
    db.commit()
    print("Naran added")