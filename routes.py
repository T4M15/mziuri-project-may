from ext import app, db
from flask import render_template, redirect, flash
from forms import RegisterForm, FoodForm, LoginForm
from models import Food, Review, User
from flask_login import login_user, logout_user, login_required
from os import path


@app.route("/")
def home():
    foods = Food.query.all()
    return render_template("index.html", foods=foods, role="admin")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        new_user.create()
        flash("წარმატებით დარეგისტრირდი")
        return redirect("/")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user:
            login_user(user)
            flash("წარმატებით შეხვედი საიტზე, ყოჩაღ ძმაო!")
            return redirect("/")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/add_food", methods=["GET", "POST"])
@login_required
def add_food():
    form = FoodForm()
    if form.validate_on_submit():
        new_food = Food(
            title=form.title.data,
            description=form.description.data,
            release_year=form.release_year.data
        )
        img = form.image.data
        new_food.image = img.filename
        if img:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
        new_food.create()
        flash("წარმატებით დაემატა საჭმელი")
        return redirect("/")
    return render_template("add_food.html", form=form)


@app.route("/update_food/<int:food_id>", methods=["GET", "POST"])
@login_required
def update_food(food_id):
    food = Food.query.get(food_id)
    form = FoodForm(title=food.title, description=food.description, release_year=food.release_year)
    if form.validate_on_submit():
        food.title = form.title.data
        food.description = form.description.data
        food.release_year = form.release_year.data
        image = form.image.data
        if image:
            directory = path.join(app.root_path, "static", "images", image.filename)
            image.save(directory)
            food.image = image.filename

        food.save()
        return redirect("/")
    return render_template("add_food.html", form=form)


@app.route("/delete_food/<int:food_id>")
@login_required
def delete_food(food_id):
    food = Food.query.get(food_id)
    food.delete()
    return redirect("/")


@app.route("/food/<int:food_id>")
def view_food_details(food_id):
    food = Food.query.get(food_id)
    reviews = Review.query.filter(Review.food_id == food_id).all()
    return render_template("food_details.html", food=food, reviews=reviews)