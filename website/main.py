from flask import Flask, render_template, request

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


@app.route('/', methods=["GET", "POST"])
def test():
    if request.method == "POST":
        pass
        # use like this
        # first_name = request.form.get("fname")
        #last_name = request.form.get("lname")
        # return "Your name is "+ first_name + last_name
    return render_template("Schedule.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
