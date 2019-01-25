from functools import wraps
from flask import request, jsonify
from os import environ
import jwt
import datetime

SECRET_KEY = environ.get("SECRET_KEY")


def encode_token(user_id, isAdmin=False):
    """ Write this later """
    payload = {
        "uid": user_id,
        "adm": isAdmin,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=3)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256").decode("utf-8")
    return token


def decoded_token(token):
    """ Write this later """
    decoded = jwt.decode(token, SECRET_KEY, algorithms="HS256")
    return decoded


def extract_token_from_header():
    """Get token fromm the headers"""
    authorization_header = request.headers.get("Authorization")
    if not authorization_header or "Bearer" not in authorization_header:
        return jsonify({
            "error": "Bad authorization header",
            "status": 400
        })
    token = authorization_header.split(" ")[1]
    return token


def token_required(func):
    """Only requests with Authorization headers required"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = None
        try:
            extract_token_from_header()
            response = func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            response = jsonify({
                "error": "Your token expired",
                "status": 401
            }), 401
        except jwt.InvalidTokenError:
            response = jsonify({
                "error": "Invalid token",
                "status": 401
            }), 401
        return response
    return wrapper


def get_current_identity():
    """Get user_id from the token"""
    return decoded_token(extract_token_from_header())["uid"]


def get_current_role():
    """Get user_role from the token"""
    return decoded_token(extract_token_from_header())["adm"]


def non_admin(func):
    """Restrict the admin from accessing the resource"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if get_current_role():  # if admin
            return jsonify({
                "error": "Admin cannot access this resource",
                "status": 403
            }), 403
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    """Restrict non admin from accessing the resource"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not get_current_role():  # if non admin
            return jsonify({
                "error": "Only Admin can access this resource",
                "status": 403
            }), 403
        return func(*args, **kwargs)
    return wrapper


def json_data_required(func):
    """Only requests with Content-type json will be allowed"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return jsonify({
                "status": 400,
                "error": "JSON request required"
            }), 400
        return func(*args, **kwargs)
    return wrapper
