from common.http import ok, bad_request, created
from routes.Auth import auth_service


def login(data):

    result, error = auth_service.login(data)

    if error:
        return bad_request(
            message="Credenciales inválidas",
            errors=error
        )

    return ok(
        data=result,
        message="Login exitoso"
    )


def register(data):

    result, error = auth_service.register(data)

    if error:
        return bad_request(
            message="Error registrando usuario",
            errors=error
        )

    return created(
        data=result,
        message="Usuario creado correctamente"
    )


def get_users():

    result, error = auth_service.get_users()

    if error:
        return bad_request(
            message="Error obteniendo usuarios",
            errors=error
        )

    return ok(
        data=result,
        message="Usuarios obtenidos"
    )


def delete_user(user_id):

    result, error = auth_service.delete_user(user_id)

    if error:
        return bad_request(
            message="Error eliminando usuario",
            errors=error
        )

    return ok(
        data={"deleted": result},
        message="Usuario eliminado"
    )


def update_user(user_id, data):

    result, error = auth_service.update_user(
        user_id,
        data
    )

    if error:
        return bad_request(
            message="Error actualizando usuario",
            errors=error
        )

    return ok(
        data=result,
        message="Usuario actualizado"
    )