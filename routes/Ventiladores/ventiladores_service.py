from typing import Any, Dict, Tuple, Optional
from contextlib import contextmanager

from db.db import SessionLocal
from db.models import Ventilator, Patient, Measurement


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_all() -> Tuple[list[Ventilator], Any]:
    with get_db() as db:
        ventiladores = db.query(Ventilator).all()
        return ventiladores, None
    
def create(data: Dict[str, Any]) -> Tuple[Optional[Ventilator], Any]:

    with get_db() as db:
        modelo = (data.get("modelo") or "").strip()
        marca = (data.get("marca") or "").strip()
        ubicacion = (data.get("ubicacion") or "").strip()
        patient_id = data.get("patient_id")

        if not modelo:
            return None, {"modelo": "Modelo es requerido"}
        if not marca:
            return None, {"marca": "Marca es requerida"}

        if patient_id:
            patient = db.query(Patient).filter(Patient.id == patient_id).first()
            if not patient:
                return None, {"patient_id": "Paciente no existe"}

        ventilador = Ventilator(
            modelo=modelo,
            marca=marca,
            ubicacion=ubicacion,
            patient_id=patient_id
        )
        db.add(ventilador)
        db.commit()
        db.refresh(ventilador)
        return ventilador, None

def delete(ventilador_id: int) -> Tuple[Optional[bool], Any]:

    with get_db() as db:
        ventilador = db.query(Ventilator).filter(Ventilator.id == ventilador_id).first()
        if not ventilador:
            return None, {"id": "Ventilador no encontrado"}

        measurement_exist = db.query(Measurement).filter(Measurement.ventilator_id == ventilador_id).first()
        if measurement_exist:
            return None, {"id": "Ventilador tiene mediciones registradas"}
        
        db.delete(ventilador)
        db.commit()
        return True, None