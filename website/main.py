from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/Home.html")


@app.route("/Home.html")
def home():
    return render_template("Home.html")


@app.route("/Changelog.html")
def changelog():
    return render_template("Changelog.html")


@app.route("/Water Amount.html")
def water_amount():
    return render_template("Water Amount.html")


@app.route('/Schedule.html', methods=["GET", "POST"])
def schedule():
    if request.method == "POST":
        print("schedule post")
    else:
        value = 6
    return render_template("Schedule.html", value=13)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")
