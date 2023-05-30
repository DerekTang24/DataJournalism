# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path="", static_folder="static")


@app.route("/")
def index():
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    canadas = []
    for e in data["Canada"].values():
        canadas.append(e)
    uss = []
    for e in data["United States"].values():
        uss.append(e)
    mexicos = []
    for e in data["Mexico"].values():
        mexicos.append(e)
    points1 = []
    for i in range(len(canadas) - 1):
        points1.append([canadas[i], canadas[i + 1]])
    points2 = []
    for i in range(len(uss) - 1):
        points2.append([uss[i], uss[i + 1]])
    points3 = []
    for i in range(len(mexicos) - 1):
        points3.append([mexicos[i], mexicos[i + 1]])

    ages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    years = [1960, 1970, 1980, 1990, 2000, 2010, 2020]

    return render_template(
        "index.html",
        years=data["Canada"].keys(),
        canada=points1,
        us=points2,
        mexico=points3,
        ages=ages,
        years2=years,
    )


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


app.run(debug=True)
