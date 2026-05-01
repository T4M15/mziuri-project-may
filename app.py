from flask import Flask, render_template

app = Flask(__name__)

foods = [
    {"type": "healthy", "disc": "Healthy food keeps your body strong and full of energy.", "img": "h1.jpg"},
    {"type": "fastfood", "disc": "Fast food is tasty and quick, but often unhealthy if eaten too much.", "img": "f1.jpg"},
    {"type": "fitness", "disc": "Protein-rich food helps build muscles and keeps you strong and active.", "img": "j1.jpg"}
]


@app.route("/")
def home():
    return render_template("home.html", foods=foods)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/foodinfo")
def foods_info():
    return render_template("foods_info.html")

@app.route("/foodinfo1")
def foods_info1():
    return render_template("foods_info1.html")

@app.route("/foodinfo2")
def foods_info2():
    return render_template("foods_info2.html")


app.run(debug=True)