from flask import Blueprint, jsonify
from app.helpers.database import Database
from app.helpers.authetication import token_required, admin_required
from app.models.user import User

get_users = Blueprint("get_users", __name__, url_prefix="/api/v1")

@get_users.route("/users", methods=["GET"])
@token_required
@admin_required
def get_all_registered_users():
    """Get all registered users"""
    users = User.get_users()
    return jsonify({
        "status": 200,
        "data": [{
            "Number of users": len(users),
            "users": users
        }]
    })