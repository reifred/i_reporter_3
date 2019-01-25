from flask import Blueprint, jsonify
from app.helpers.authetication import token_required
from app.models.incident import Incident

from app.helpers.validators import valid_url_input, set_incident_type

get_records = Blueprint("get_records", __name__, url_prefix="/api/v1")


@get_records.route("/<string:incident_type>", methods=["GET"])
@token_required
def get_all_records(incident_type):
    """Get available incidents"""
    if not valid_url_input(incident_type):
        return jsonify({
            "status": 404,
            "error": "Page Not found. Enter a valid URL"
        }), 404

    _type = set_incident_type(incident_type)

    red_flag_records = Incident.get_records(_type)
    return jsonify({
        "data": red_flag_records,
        "status": 200
    }), 200
