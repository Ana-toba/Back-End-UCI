from common.http import ok, bad_request, created
from routes.Pacientes import pacientes_service


def get_all():
    data, error = pacientes_service.get_all()
    if error:
        return bad_request( message="No se pudieron obtener los pacientes", errors=error)
    return ok( data=[pacientes.to_dict() for pacientes in data], message="Pacientes obtenidos con éxito")

def create(data):
    result, error = pacientes_service.create(data)
    if error:
        return bad_request(message="Error creando paciente",errors=error)

    return created(data=result.to_dict(),message="Paciente creado con éxito")

def delete(pacientes_id: int):
    result, error = pacientes_service.delete(pacientes_id)
    if error:
        return bad_request( message="Error eliminando paciente", errors=error)
    return ok( data={"deleted": result}, message="Paciente eliminado con éxito")

def update(paciente_id: int, data):

    result, error = pacientes_service.update(
        paciente_id,
        data
    )

    if error:
        return bad_request(
            message="Error actualizando paciente",
            errors=error
        )

    return ok(
        data=result.to_dict(),
        message="Paciente actualizado con éxito"
    )