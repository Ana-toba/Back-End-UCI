#Imports de estructura 
import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from datetime import timedelta

##Indicando las rutas de acceso
from routes.Ventiladores.ventiladores_routes import ventiladores_bp
from routes.Pacientes.pacientes_routes import pacientes_bp
from routes.Mediciones.mediciones_routes import mediciones_bp
from routes.Auth.auth_routes import auth_bp
from routes.Realtime.realtime_routes import realtime_bp

#Configuraciones de la aplicación
def run_app():

    load_dotenv()

    app = Flask(__name__)

    #JWT
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(
        minutes=int(os.getenv("JWT_EXPIRES_MIN", 60))
    )

    jwt = JWTManager(app)

    #CORS
    CORS(
        app,
        resources={r"/*":{"origins": "*"}},
        supports_credentials=False,
        expose_headers=["Authorization"],
        allow_headers=["content-type", "Authorization"],
        methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    )
    
    ### Registrar rutas
    app.register_blueprint(ventiladores_bp)
    app.register_blueprint(pacientes_bp)
    app.register_blueprint(mediciones_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(realtime_bp)

    return app

app = run_app()

if __name__ == "__main__":

    app.run(
        host=os.getenv("HOST","127.0.0.1"),
        port=int(os.getenv("PORT", 5000)),
        debug=True
    )