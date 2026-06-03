from ext import app, db
from flask import render_template, redirect, abort
from forms import RegisterForm, FoodForm
from models import Food
from os import path

profiles = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/foodinfo")
def food_info():
    return render_template("foodinfo.html")


@app.route("/foodinfo1")
def food_info1():
    return render_template("foodinfo1.html")


@app.route("/foodinfo2")
def food_info2():
    return render_template("foodinfo2.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = {
            "username": form.username.data,
            "mobile": form.mobile.data,
            "date": form.birthdate.data,
        }
        img = form.image.data
        if img:
            directory = path.join(app.root_path, "static", "images", img.filename)
            new_user["img"] = img.filename
            img.save(directory)
        profiles.append(new_user)
        return redirect("/")
    return render_template("register.html", form=form)


@app.route("/add_food", methods=["GET", "POST"])
def add_food():
    form = FoodForm()
    if form.validate_on_submit():
        new_food = Food(title=form.title.data, description=form.description.data)
        img = form.image.data
        if img:
            new_food.image = img.filename
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)

        new_food.create()
        return redirect("/")
    return render_template("add_food.html", form=form)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    try:
        prof = profiles[profile_id]
        return render_template("profile.html", profile=prof)
    except IndexError:
        abort(404)