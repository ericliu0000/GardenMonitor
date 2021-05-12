from flask import Flask, render_template

app = Flask(__name__)

@app.route("/Home.html")
def index():
    return render_template("Home.html")

@app.route("/Changelog.html")
def changelog():
    return render_template("Changelog.html")

@app.route("/Schedule.html")
def schedule():
    return render_template("Schedule.html")

@app.route("/Water Amount.html")
def water_amount():
    return render_template("Water Amount.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")