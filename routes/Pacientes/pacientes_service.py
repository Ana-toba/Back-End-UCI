from typing import Any, Dict, Tuple, Optional
from contextlib import contextmanager
from datetime import datetime

from db.db import SessionLocal
from db.models import Patient, Measurement


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_all() -> Tuple[list[Patient], Any]:
    with get_db() as db:
        patients = db.query(Patient).all()
        return patients, None
    

def create(data: Dict[str, Any]) -> Tuple[Optional[Patient], Any]:
    with get_db() as db:
        nombre = (data.get("nombre") or "").strip()
        apellido = (data.get("apellido") or "").strip()
        edad = data.get("edad")
        sexo = (data.get("sexo") or "").strip()
        numero_historia = (data.get("numero_historia") or "").strip()
        cama = data.get("cama")

        if not nombre:
            return None, {"nombre": "Nombre es requerido"}
        if not apellido:
            return None, {"apellido": "Apellido es requerido"}
        if edad is None:
            return None, {"edad": "Edad es requerida"}
        if not sexo:
            return None, {"sexo": "Sexo es requerido"}

        if numero_historia:
            exist = db.query(Patient).filter(Patient.numero_historia == numero_historia).first()
            if exist:
                return None, {"numero_historia": "Ya existe"}

        patient = Patient(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            sexo=sexo,
            numero_historia=numero_historia,
            cama=cama,
            fecha_ingreso=datetime.now()
        )
        db.add(patient)
        db.commit()
        db.refresh(patient)
        return patient, None

def delete(paciente_id: int) -> Tuple[bool, Any]:

    with get_db() as db:

        patient = db.query(Patient).filter(Patient.id == paciente_id).first()

        if not patient:
            return False, {"patient": "Paciente no encontrado"}

        db.delete(patient)
        db.commit()

        return True, None


def update(paciente_id: int, data: Dict[str, Any]) -> Tuple[Optional[Patient], Any]:

    with get_db() as db:

        patient = db.query(Patient).filter(Patient.id == paciente_id).first()

        if not patient:
            return None, {"patient": "Paciente no encontrado"}

        nombre = (data.get("nombre") or patient.nombre).strip()
        apellido = (data.get("apellido") or patient.apellido).strip()
        edad = data.get("edad", patient.edad)
        sexo = (data.get("sexo") or patient.sexo).strip()
        numero_historia = (
            data.get("numero_historia") or patient.numero_historia
        )
        cama = data.get("cama", patient.cama)

        if not nombre:
            return None, {"nombre": "Nombre es requerido"}

        if not apellido:
            return None, {"apellido": "Apellido es requerido"}

        if edad is None:
            return None, {"edad": "Edad es requerida"}

        if not sexo:
            return None, {"sexo": "Sexo es requerido"}

        if numero_historia:

            exist = (
                db.query(Patient)
                .filter(
                    Patient.numero_historia == numero_historia,
                    Patient.id != paciente_id
                )
                .first()
            )

            if exist:
                return None, {
                    "numero_historia": "Ya existe"
                }

        patient.nombre = nombre
        patient.apellido = apellido
        patient.edad = edad
        patient.sexo = sexo
        patient.numero_historia = numero_historia
        patient.cama = cama

        db.commit()
        db.refresh(patient)

        return patient, None