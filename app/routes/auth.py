from flask import Blueprint, jsonify, request
from app.models.user import User
from datetime import datetime
from app.helpers.database import Database
from app.helpers.validators import validate_user_input, validate_sign_in

from app.helpers.authetication import (
    encode_token,
    token_required,
    admin_required,
    json_data_required
)

from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/api/v1")

response = None


@auth_bp.route("/auth/sign_up", methods=["POST"])
@json_data_required
def sign_up():
    """Function to register a new user"""
    user = request.get_json()
    user["registered"] = datetime.now().strftime("%Y-%m-%d")

    firstname = user.get("firstname")
    lastname = user.get("lastname")
    email = user.get("email")
    phoneNumber = user.get("phoneNumber")
    username = user.get("username")
    password = user.get("password")

    user_exists = User.user_exists(username, email)

    errors = validate_user_input(
        firstname, lastname, email, phoneNumber,
        username, password
    )

    if errors:
        response = jsonify({"status": 400, "error": errors}), 400
    elif user_exists:
        response = jsonify({"status": 400,
                            "error": "username or email already exists"
                            }), 400
    else:
        user["password"] = generate_password_hash(
            user["password"], method="sha256")

        guest = User(**user)
        User.register_user(**guest.convert_to_dict())
        user_id = User.user_exists(username)[0]["id"]
        response = jsonify({
            "status": 201,
            "data": [{
                "id": user_id,
                "user": guest.convert_to_dict(),
                "message": "User registered"
            }]
        }), 201
    return response


@auth_bp.route("/auth/sign_in", methods=["POST"])
@json_data_required
def sign_in():
    """Function to login a user"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    errors = validate_sign_in(username, password)

    if errors:
        response = jsonify({"status": 400, "error": errors}), 400
    else:
        username_exists = User.user_exists(username)
        if not username_exists:
            response = jsonify({
                "status": 400,
                "error": "Username doesnt exist"
            }), 400
        elif not check_password_hash(username_exists[0]["password"], password):
            response = jsonify({
                "status": 400,
                "error": "Enter correct password"
            }), 400
        else:
            user_id = username_exists[0]["id"]
            user_adm = username_exists[0]["isadmin"]
            token = encode_token(user_id, user_adm)
            response = jsonify({
                "status": 201,
                "data": [{
                    "id": user_id,
                    "message": "User login",
                    "user": username_exists[0],
                    "token": token
                }]
            }), 201

    return response
