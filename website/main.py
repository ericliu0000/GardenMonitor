from flask import Flask, render_template, request, redirect
import sqlite3
import datetime


app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/Home.html")


@app.route("/Home.html")
def home():
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("/Home.html", time=currentTime)


@app.route("/Changelog.html")
def changelog():
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("/Changelog.html", time=currentTime)


@app.route("/Water Amount.html")
def water_amount():
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("/Water Amount.html", time=currentTime)


@app.route('/Schedule.html', methods=["GET", "POST"])
def schedule():
    interval = 6
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == "POST":
        print("Got a response")
        try:
            interval = int(request.form["text"])
            print(interval)
            return render_template("/Schedule.html", time = currentTime, status = f"Successfully set interval to {interval} hours.")
        except:
            return render_template("/Schedule.html", time = currentTime, status = f"Something went wrong! Interval still at {interval} hours.")
    return render_template("/Schedule.html", time = currentTime, status = f"Interval is {interval} hours.")

@app.route('/Water Amount.html', methods = ["GET", "POST"])
def waterAmount():
    amount = 0
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == "POST":
        print("Got a response")
        try:
            amount = int(request.form["text"])
            print(amount)
            return render_template("/Water Amount.html", time = currentTime, status = f"Successfully set Water Amount to {amount} mL")
        except:
            return render_template("/Water Amount.html", time = currentTime, status = f"Something went wrong! Water Amount still at {amount} mL")
    return render_template("/Water Amount.html", time = currentTime, status = f"Water Amount is {amount} mL")


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")