from flask import Blueprint, request
from routes.Pacientes import pacientes_controllers

pacientes_bp = Blueprint(
    "pacientes_bp",
    __name__,
    url_prefix="/Pacientes"
)

@pacientes_bp.route("/get", methods=["GET"])
def get_all():
    return pacientes_controllers.get_all()


@pacientes_bp.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    return pacientes_controllers.create(data)


@pacientes_bp.route("/update/<int:paciente_id>", methods=["PUT"])
def update(paciente_id):

    data = request.get_json()

    return pacientes_controllers.update(
        paciente_id,
        data
    )


@pacientes_bp.route("/delete/<int:paciente_id>", methods=["DELETE"])
def delete(paciente_id):

    return pacientes_controllers.delete(
        paciente_id
    )