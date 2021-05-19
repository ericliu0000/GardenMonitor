from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/Home.html")

@app.route("/Home.html")
def home():
    import datetime
    current = datetime.datetime.now()
    currentTime = current.strftime("%Y-%m-%d %H:%M:%S")
    return render_template("/Home.html", time = currentTime)

@app.route("/Changelog.html")
def changelog():
    import datetime
    current = datetime.datetime.now()
    currentTime = current.strftime("%Y-%m-%d %H:%M:%S")
    return render_template("/Changelog.html", time = currentTime)

@app.route("/Water Amount.html")
def water_amount():
    import datetime
    current = datetime.datetime.now()
    currentTime = current.strftime("%Y-%m-%d %H:%M:%S")
    return render_template("/Water Amount.html", time = currentTime)

@app.route('/Schedule.html', methods=["GET", "POST"])
def schedule():
    import datetime
    current = datetime.datetime.now()
    currentTime = current.strftime("%Y-%m-%d %H:%M:%S")
    return render_template("/Schedule.html", time = currentTime)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")
