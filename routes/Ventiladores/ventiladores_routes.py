from flask import Blueprint, request
from routes.Ventiladores import ventiladores_controllers

ventiladores_bp = Blueprint("ventiladores_bp", __name__, url_prefix="/ventiladores")

@ventiladores_bp.route("/get", methods=["GET"])
def get_all():
    return ventiladores_controllers.get_all()

@ventiladores_bp.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    return ventiladores_controllers.create(data)

@ventiladores_bp.route("/delete/<int:ventilador_id>", methods=["DELETE"])
def delete(ventilador_id):
    return ventiladores_controllers.delete(ventilador_id)