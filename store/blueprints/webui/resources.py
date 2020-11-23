import requests
import csv
import pandas as pd
from flask import Blueprint, render_template, url_for, request, jsonify, redirect

bp = Blueprint("webui", __name__, url_prefix="/", template_folder="templates", static_folder="static", static_url_path='/static/webui')

@bp.route("/", methods=["GET"])
def index():
        r = requests.get(f"{request.host_url}api/")
        return render_template("index.html", title="Dafiti Challenge", json=r.json())

@bp.route("/insert", methods=["GET", "POST"])
def insertManualy():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        description = request.form["description"]
        json = {
            "name": name,
            "price": price,
            "description": description
        }
        requests.post(f"{request.host_url}api/", json=json)
        return redirect(url_for("webui.index"))
    else:
        return redirect(url_for("webui.index"))

@bp.route("/insertmany", methods=["GET", "POST"])
def insertMany():
    if request.method == "POST":
        f = request.files["file"]
        pandas_as_list = pd.read_csv(f).values.tolist()
        for element in pandas_as_list:
            json = {
                "name": element[0],
                "price": element[1],
                "description": element[2]
            }
            requests.post(f"{request.host_url}api/", json=json)
        return redirect(url_for("webui.index"))
    else:
        return redirect(url_for("webui.index"))

@bp.route("/update/<int:identifier>", methods=["GET", "POST"])
def update(identifier):
    update = requests.get(f"{request.host_url}api/{identifier}")
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        description = request.form["description"]
        json = {
            "name": name,
            "price": price,
            "description": description
        }
        requests.put(f"{request.host_url}api/{identifier}", json=json)
        return redirect(url_for("webui.index"))
    else:
        return render_template("update.html", title="Dafiti Challenge", update=update.json()[0])

@bp.route("/delete", methods=["GET"])
def rawdelete():
    return redirect(url_for("webui.index"))

@bp.route("/delete/<int:identifier>", methods=["GET"])
def delete(identifier):
    delete = requests.get(f"{request.host_url}api/{identifier}")
    requests.delete(f"{request.host_url}api/{identifier}")
    return redirect(url_for("webui.index"))
