from flask import Blueprint, jsonify

home = Blueprint("home", __name__, url_prefix="/api/v1")

@home.route("/")
def index():
    """Home route"""
    return jsonify({
        "status": 200,
        "message": "Welcome to api."
    }) 