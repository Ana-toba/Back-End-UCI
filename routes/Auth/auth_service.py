from contextlib import contextmanager
from datetime import datetime
from flask_jwt_extended import create_access_token

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from db.db import SessionLocal
from db.models import User, Role


@contextmanager
def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def login(data):

    with get_db() as db:

        email = data.get("email")
        password = data.get("password")

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            return None, {
                "email": "Usuario no encontrado"
            }

        if not check_password_hash(
            user.password,
            password
        ):
            return None, {
                "password": "Contraseña incorrecta"
            }

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "role": user.role_relation.nombre
            }
        )

        return {
            "access_token": access_token,
            "user": {
                "id": user.id,
                "nombre": user.nombre,
                "apellido": user.apellido,
                "email": user.email,
                "role": user.role_relation.nombre
            }
        }, None

def register(data):

    with get_db() as db:

        email = data.get("email")

        exist = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if exist:
            return None, {
                "email": "El correo ya existe"
            }

        hashed_password = generate_password_hash(
            data.get("password")
        )

        user = User(
            nombre=data.get("nombre"),
            apellido=data.get("apellido"),
            email=email,
            password=hashed_password,
            role_id=data.get("role_id"),
            created_at=datetime.now()
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return user.to_dict(), None


def get_users():

    with get_db() as db:

        users = db.query(User).all()

        return [u.to_dict() for u in users], None


def delete_user(user_id):

    with get_db() as db:

        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            return None, {
                "user": "Usuario no encontrado"
            }

        db.delete(user)

        db.commit()

        return True, None


def update_user(user_id, data):

    with get_db() as db:

        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            return None, {
                "user": "Usuario no encontrado"
            }

        user.nombre = data.get(
            "nombre",
            user.nombre
        )

        user.apellido = data.get(
            "apellido",
            user.apellido
        )

        user.email = data.get(
            "email",
            user.email
        )

        if data.get("password"):

            user.password = generate_password_hash(
                data.get("password")
            )

        if data.get("role_id"):

            user.role_id = data.get("role_id")

        db.commit()

        db.refresh(user)

        return user.to_dict(), None