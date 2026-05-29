from flask import Blueprint, request
from routes.Mediciones import mediciones_controllers

mediciones_bp = Blueprint("mediciones_bp", __name__, url_prefix="/Mediciones")

@mediciones_bp.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    return mediciones_controllers.create(data)

@mediciones_bp.route("/patient/<int:patient_id>", methods=["GET"])
def get_by_patient(patient_id):
    return mediciones_controllers.get_by_patient(patient_id)

@mediciones_bp.route("/latest/<int:patient_id>", methods=["GET"])
def get_latest(patient_id):
    return mediciones_controllers.get_latest(patient_id)

@mediciones_bp.route("/dashboard", methods=["GET"])
def dashboard():
    return mediciones_controllers.dashboard()

@mediciones_bp.route("/clear",methods=["DELETE"])
def clear_all():
    return mediciones_controllers.clear_all()