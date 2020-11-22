import requests
from flask import Blueprint, render_template, url_for, request, jsonify
from store.extensions import config

bp = Blueprint("webui", __name__, url_prefix="/", template_folder="templates", static_folder="static", static_url_path='/static/webui')
@bp.route("/", methods=["GET"])
def index():
    r = requests.get('http://localhost:5000/api/')
    return render_template("template.html", title="Dafiti Challenge", json=r.json())
