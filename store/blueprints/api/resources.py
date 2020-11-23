from flask import Blueprint, jsonify, request, current_app
from store.extensions.database import db
from store.extensions.database.models import Shoes
from store.extensions.serealizer.serealizer import ShoeSchema

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/", methods=["GET"])
def get():
    """Get all registered shoes in database""" 
    bs = ShoeSchema(many=True)
    result = Shoes.query.all()
    return bs.jsonify(result), 200

@bp.route("/<identifier>", methods=["GET"])
def get_by_id(identifier):
    bs = ShoeSchema(many=True)
    result = Shoes.query.filter(Shoes.id == identifier)
    return bs.jsonify(result), 200

@bp.route("/", methods=["POST"])
def post():
    """Insert a new shoe in database"""
    bs = ShoeSchema()
    shoe = bs.load(request.json)
    db.session.add(shoe)
    db.session.commit()
    return bs.jsonify(shoe), 201

@bp.route("/<identifier>", methods=["PUT"])
def put(identifier):
    """Update a existing shoe in database"""
    bs = ShoeSchema()
    query = Shoes.query.filter(Shoes.id == identifier)
    query.update(request.json)
    db.session.commit()
    if query.first():
        return bs.jsonify(query.first())
    else:
        return jsonify({"Response": "Shoe not founded"}), 404

@bp.route("/<identifier>", methods=["DELETE"])
def delete(identifier):
    """Delete a existing shoe in database"""
    query = Shoes.query.filter(Shoes.id == identifier).first()
    if query:
        Shoes.query.filter(Shoes.id == identifier).delete()
        db.session.commit()
        return jsonify({"Response": "Shoe deleted"}), 200
    else:
        return jsonify({"Response": "Shoe not founded"}), 404