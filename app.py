from ext import app, db
from models import Food

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    from routes import *

    app.run(debug=True)