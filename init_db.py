from ext import app, db
from models import Food , User


with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(username="Admin",
                 password="admin1234",
                 role="Admin")
    admin.create()
