from datetime import date
from app import create_app, db
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

app = create_app()

with app.app_context():
    # Drop and create all tables
    db.drop_all()
    db.create_all()

    # Guests
    guest1 = Guest(name="Tom Hanks", occupation="Actor")
    guest2 = Guest(name="Taylor Swift", occupation="Singer")
    guest3 = Guest(name="Serena Williams", occupation="Athlete")

    db.session.add_all([guest1, guest2, guest3])

    # Episodes
    ep1 = Episode(date=date(2024, 1, 1), number=1)
    ep2 = Episode(date=date(2024, 1, 2), number=2)

    db.session.add_all([ep1, ep2])

    # Appearances
    app1 = Appearance(guest=guest1, episode=ep1, rating=5)
    app2 = Appearance(guest=guest2, episode=ep1, rating=4)
    app3 = Appearance(guest=guest3, episode=ep2, rating=3)

    db.session.add_all([app1, app2, app3])

    db.session.commit()
    print("✅ Seeding complete.")
