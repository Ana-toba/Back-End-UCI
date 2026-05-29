from typing import Any, Dict, Tuple, Optional
from contextlib import contextmanager
from datetime import datetime
from datetime import datetime, timedelta

from db.db import SessionLocal

from db.models import (
    Measurement,
    Patient,
    Ventilator
)


# =====================================================
# DB SESSION
# =====================================================

@contextmanager
def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


# =====================================================
# PARAMETRO DINAMICO
# =====================================================

def get_dynamic_parameter_name(
    mode
):

    mapping = {

        "ASV": "%VolMin",

        "SIMV+": "Vt",

        "PCV+": "Pcontrol",

        "PSIMV+": "Pinsp"
    }

    return mapping.get(
        mode,
        "Parametro"
    )


# =====================================================
# CREATE
# =====================================================

def create(
    data: Dict[str, Any]
) -> Tuple[Optional[Measurement], Any]:

    with get_db() as db:

        # =========================================
        # VALIDAR PATIENT
        # =========================================

        patient_id = data.get(
            "patient_id"
        )

        if not patient_id:

            return None, {

                "patient_id":
                    "patient_id is required"
            }

        patient = db.query(
            Patient
        ).filter(

            Patient.id == patient_id

        ).first()

        if not patient:

            return None, {

                "patient_id":
                    "Patient not found"
            }

        # =========================================
        # CREAR MEDICION
        # =========================================

        measurement = Measurement(

            patient_id=patient_id,

            ventilator_id=data.get(
                "ventilator_id"
            ),

            fecha_hora=datetime.now(),

            modo=data.get(
                "modo"
            ),

            Ppico=data.get(
                "Ppico"
            ),

            VolMinEsp=data.get(
                "VolMinEsp"
            ),

            VTE=data.get(
                "VTE"
            ),

            fTotal=data.get(
                "fTotal"
            ),

            parametro_modo=data.get(
                "parametro_modo"
            ),

            PEEP=data.get(
                "PEEP"
            ),

            Oxigeno=data.get(
                "Oxigeno"
            )
        )

        db.add(measurement)

        db.commit()

        db.refresh(measurement)

        return measurement, None


# =====================================================
# GET BY PATIENT
# =====================================================

def get_by_patient(
    patient_id: int
) -> Tuple[list[Measurement], Any]:

    with get_db() as db:

        measurements = db.query(
            Measurement
        ).filter(

            Measurement.patient_id == patient_id

        ).order_by(

            Measurement.fecha_hora.desc()

        ).all()

        return measurements, None


# =====================================================
# GET LATEST
# =====================================================

def get_latest(
    patient_id: int
) -> Tuple[Optional[Measurement], Any]:

    with get_db() as db:

        measurement = db.query(
            Measurement
        ).filter(

            Measurement.patient_id == patient_id

        ).order_by(

            Measurement.fecha_hora.desc()

        ).first()

        return measurement, None


# =====================================================
# DASHBOARD
# =====================================================

def dashboard():

    with get_db() as db:

        ventilators = db.query(
            Ventilator
        ).all()

        dashboard_data = []

        for vent in ventilators:

            latest = (

                db.query(Measurement)

                .filter(

                    Measurement.ventilator_id
                    == vent.id
                )

                .order_by(

                    Measurement.fecha_hora
                    .desc()

                )

                .first()
            )

            # =====================================
            # TIMEOUT 3 SEGUNDOS
            # =====================================

            if latest:

                diff = (

                    datetime.now()

                    - latest.fecha_hora

                ).total_seconds()

                if diff > 3:

                    latest = None

            # =====================================
            # SI TIENE DATOS RECIENTES
            # =====================================

            if latest:

                dashboard_data.append({

                    "id":
                        vent.id,

                    "cama":
                        vent.ubicacion,

                    "modo":
                        latest.modo,

                    "nombreParametro":

                        get_dynamic_parameter_name(

                            latest.modo
                        ),

                    "valorParametro":
                        latest.parametro_modo,

                    "Ppico":
                        latest.Ppico,

                    "VolMinEsp":
                        latest.VolMinEsp,

                    "VTE":
                        latest.VTE,

                    "fTotal":
                        latest.fTotal,

                    "PEEP":
                        latest.PEEP,

                    "Oxigeno":
                        latest.Oxigeno,

                    "activo":
                        True
                })

            # =====================================
            # SIN DATOS O DATOS VIEJOS
            # =====================================

            else:

                dashboard_data.append({

                    "id":
                        vent.id,

                    "cama":
                        vent.ubicacion,

                    "modo":
                        "--",

                    "nombreParametro":
                        "--",

                    "valorParametro":
                        "--",

                    "Ppico":
                        "--",

                    "VolMinEsp":
                        "--",

                    "VTE":
                        "--",

                    "fTotal":
                        "--",

                    "PEEP":
                        "--",

                    "Oxigeno":
                        "--",

                    "activo":
                        False
                })

        return dashboard_data, None
    
# =====================================================
# CLEAR ALL
# =====================================================

def clear_all():

    with get_db() as db:

        db.query(
            Measurement
        ).delete()

        db.commit()

        return True, None