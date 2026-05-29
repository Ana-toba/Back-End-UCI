from flask import Blueprint, request
from routes.Auth import auth_controllers

auth_bp = Blueprint(
    "auth_bp",
    __name__,
    url_prefix="/Auth"
)

# Login
@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    return auth_controllers.login(data)


# Register
@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    return auth_controllers.register(data)


# Get users
@auth_bp.route("/get", methods=["GET"])
def get_users():

    return auth_controllers.get_users()


# Delete user
@auth_bp.route("/delete/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    return auth_controllers.delete_user(user_id)


# Update user
@auth_bp.route("/update/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    data = request.get_json()

    return auth_controllers.update_user(
        user_id,
        data
    )