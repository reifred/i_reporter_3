from app.helpers.database import Database
from flask import Blueprint, jsonify
from app.helpers.database import Database
from app.helpers.authetication import token_required
from app.models.incident import Incident

get_records = Blueprint("get_records", __name__, url_prefix="/api/v1")


@get_records.route("/<string:incident_type>", methods=["GET"])
@token_required
def get_all_records(incident_type):
    """Get available red flags"""

    if incident_type not in ["red_flags", "interventions"]:
        return jsonify({
            "status": 404,
            "error": "Page Not found. Enter a valid URL"
        }), 404

    if incident_type == "red_flags":
        _type = "red-flag"
    elif incident_type == "interventions":
        _type = "intervention"

    red_flag_records = Incident.get_records(_type)
    return jsonify({
        "data": red_flag_records,
        "status": 200
    }), 200
