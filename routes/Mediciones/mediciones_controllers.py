from common.http import ok, bad_request, created
from routes.Mediciones import mediciones_service


def create(data):
    result, error = mediciones_service.create(data)

    if error:
        return bad_request(message="Error creando medición",errors=error)
    return created(data=result.to_dict(),message="Medición creada con éxito")

def get_by_patient(patient_id: int):
    data, error = mediciones_service.get_by_patient(patient_id)

    if error:
        return bad_request(message="Error obteniendo mediciones",errors=error)
    return ok(
        data=[m.to_dict() for m in data], message="Mediciones obtenidas con éxito")

def get_latest(patient_id: int):
    result, error = mediciones_service.get_latest(patient_id)

    if error:
        return bad_request(message="Error obteniendo última medición", errors=error)
    return ok(
        data=result.to_dict() if result else None, message="Última medición obtenida")


def dashboard():
    data, error = mediciones_service.dashboard()

    if error:
        return bad_request(
            message="Error obteniendo dashboard",
            errors=error
        )

    return ok(
        data=data,
        message="Dashboard obtenido"
    )

def clear_all():

    _, error = mediciones_service.clear_all()

    if error:

        return bad_request(
            message="Error eliminando mediciones",
            errors=error
        )

    return ok(
        message="Mediciones eliminadas"
    )