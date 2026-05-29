from common.http import ok, bad_request, created
from routes.Ventiladores import ventiladores_service


def get_all():
    data, error = ventiladores_service.get_all()
    if error:
        return bad_request(
            message="No se pudieron obtener los ventiladores",
            errors=error
        )
    return ok(data=[v.to_dict() for v in data],message="Ventiladores obtenidos con éxito")

def create(data):
    result, error = ventiladores_service.create(data)

    if error:
        return bad_request( message="Error creando ventilador", errors=error)
    return created( data=result.to_dict(), message="Ventilador creado con éxito")

def delete(ventilador_id: int):
    result, error = ventiladores_service.delete(ventilador_id)

    if error:
        return bad_request( message="Error eliminando ventilador", errors=error)
    return ok( data={"deleted": result}, message="Ventilador eliminado con éxito")