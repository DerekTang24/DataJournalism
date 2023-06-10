# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import json


app = Flask(__name__, static_url_path="", static_folder="static")


@app.route("/")
def index():
    return redirect("/about", code=302)


@app.route("/year")
def year():
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()

    year = request.args.get("year")

    mexico = 90 - ((data["Mexico"][year]) - 50) * 2
    canada = 90 - ((data["Canada"][year]) - 50) * 2
    us = 90 - ((data["United States"][year]) - 50) * 2

    years = [
        ["Mexico", data["Mexico"][year]],
        ["Canada", data["Canada"][year]],
        ["United States", data["United States"][year]],
    ]

    return render_template(
        "year.html", year=year, mexico=mexico, us=us, canada=canada, years=years
    )


@app.route("/about")
def about():

    return render_template("about.html")

@app.route("/macro")
def macro():
    
    return render_template("macro.html")


app.run(debug=True)
