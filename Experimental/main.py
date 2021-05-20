from flask import Flask, render_template, request, redirect
import sqlite3
import datetime

app = Flask(__name__)

global interval
interval = 6


@app.route("/")
def index():
    return redirect("/Schedule.html")


@app.route('/Schedule.html', methods=["GET", "POST"])
def schedule():
    interval = 6
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == "POST":
        print("Got a response")
        try:
            interval = int(request.form["text"])
            print(interval)
            return render_template("/Schedule.html", time=currentTime, status=f"Successfully set interval to {interval} hours.")
        except:
            return render_template("/Schedule.html", time=currentTime, status="Something wrong!")
    return render_template("/Schedule.html", time=currentTime, status=f"Interval is {interval} hours.")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
