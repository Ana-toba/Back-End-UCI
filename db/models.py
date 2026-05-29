from __future__ import annotations

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Float,
    Boolean
)

from sqlalchemy.orm import relationship

from db.db import base


# =========================
# ROLES
# =========================

class Role(base):

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)

    nombre = Column(String(50), unique=True, nullable=False)

    usuarios = relationship(
        "User",
        back_populates="role_relation"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "nombre": self.nombre
        }


# =========================
# USERS
# =========================

class User(base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    nombre = Column(String(100), nullable=False)

    apellido = Column(String(100), nullable=False)

    email = Column(String(120), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    activo = Column(Boolean, default=True)

    role_id = Column(
        Integer,
        ForeignKey("roles.id"),
        nullable=False
    )

    role_relation = relationship(
        "Role",
        back_populates="usuarios"
    )

    created_at = Column(DateTime)

    def to_dict(self):

        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "activo": self.activo,
            "role": (
                self.role_relation.nombre
                if self.role_relation
                else None
            )
        }


# =========================
# PATIENTS
# =========================

class Patient(base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)

    nombre = Column(String(100), nullable=False)

    apellido = Column(String(100), nullable=False)

    edad = Column(Integer, nullable=False)

    sexo = Column(String(10), nullable=False)

    numero_historia = Column(String(50), unique=True)

    cama = Column(String(10))

    fecha_ingreso = Column(DateTime)

    ventiladores = relationship(
        "Ventilator",
        back_populates="patient_relation"
    )

    mediciones = relationship(
        "Measurement",
        back_populates="patient_relation"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "sexo": self.sexo,
            "cama": self.cama
        }


# =========================
# VENTILATORS
# =========================

class Ventilator(base):

    __tablename__ = "ventilators"

    id = Column(Integer, primary_key=True)

    modelo = Column(String(50))

    marca = Column(String(50))

    ubicacion = Column(String(50))

    patient_id = Column(
        Integer,
        ForeignKey("patients.id")
    )

    patient_relation = relationship(
        "Patient",
        back_populates="ventiladores"
    )

    mediciones = relationship(
        "Measurement",
        back_populates="ventilator_relation"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "modelo": self.modelo,
            "marca": self.marca,
            "ubicacion": self.ubicacion,
            "patient_id": self.patient_id
        }


# =========================
# MEASUREMENTS
# =========================

class Measurement(base):

    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    ventilator_id = Column(
        Integer,
        ForeignKey("ventilators.id")
    )

    modo = Column(String(20))

    Ppico = Column(Float)

    VolMinEsp = Column(Float)

    VTE = Column(Float)

    fTotal = Column(Float)

    parametro_modo = Column(Float)

    PEEP = Column(Float)

    Oxigeno = Column(Float)

    fecha_hora = Column(
        DateTime,
        nullable=False
    )

    patient_relation = relationship(
        "Patient",
        back_populates="mediciones"
    )

    ventilator_relation = relationship(
        "Ventilator",
        back_populates="mediciones"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "ventilator_id": self.ventilator_id,
            "fecha_hora": self.fecha_hora,
            "modo": self.modo,
            "Ppico": self.Ppico,
            "VolMinEsp": self.VolMinEsp,
            "VTE": self.VTE,
            "fTotal": self.fTotal,
            "parametro_modo": self.parametro_modo,
            "PEEP": self.PEEP,
            "Oxigeno": self.Oxigeno
        }