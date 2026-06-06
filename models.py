from sqlalchemy import ForeignKey
from flask_login import UserMixin
from ext import db , login_manager

class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

class User(BaseModel ,db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

    return User.query.get(int(user_id))
class Food(db.Model, BaseModel):
    __tablename__ = "foods"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)
    image = db.Column(db.String(), default="default_image.jpg")

class Review(db.Model, BaseModel):
    __tablename__ = "reviews"

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(), nullable=False)
    food_id = db.Column(ForeignKey("foods.id"))