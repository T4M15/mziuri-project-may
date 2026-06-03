from ext import app, db
from models import Food

with app.app_context():
    db.create_all()