from flask import Blueprint
from flask import jsonify
from flask import request

import time

realtime_bp = Blueprint(

    "realtime_bp",

    __name__,

    url_prefix="/realtime"
)

# =========================================
# VARIABLES GLOBALES
# =========================================

latest_data = None

last_update = 0

TIMEOUT_SECONDS = 2

# =========================================
# UPDATE REALTIME
# =========================================

@realtime_bp.route(

    "/update",

    methods=["POST"]
)
def realtime_update():

    global latest_data
    global last_update

    latest_data = request.json

    last_update = time.time()

    print("\nREALTIME:")
    print(latest_data)

    return jsonify({

        "status": "ok"
    })

# =========================================
# GET REALTIME
# =========================================

@realtime_bp.route(

    "/latest",

    methods=["GET"]
)
def realtime_latest():

    global latest_data
    global last_update

    # =====================================
    # LIMPIAR SI main_video SE DETIENE
    # =====================================

    if (

        time.time() - last_update

        > TIMEOUT_SECONDS

    ):

        latest_data = None

    return jsonify({

        "data": latest_data
    })