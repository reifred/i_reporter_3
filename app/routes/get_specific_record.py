from flask import Blueprint, jsonify
from app.helpers.authetication import token_required
from app.models.incident import Incident

from app.helpers.validators import valid_url_input, set_incident_type

get_single_record = Blueprint(
    "get_single_record", __name__, url_prefix="/api/v1")

response = None


@get_single_record.route(
    "/<string:incident_type>/<int:incident_id>", methods=["GET"])
@token_required
def get_single_red_flag_of_id(incident_type, incident_id):
    """Get a red flag of id incident_id"""

    if not valid_url_input(incident_type):
        return jsonify({
            "status": 404,
            "error": "Page Not found. Enter a valid URL"
        }), 404

    _type = set_incident_type(incident_type)

    incident_of_id = Incident.get_specific_record(incident_id, _type)
    if not incident_of_id:
        response = jsonify({
            "status": 400,
            "error": f"{_type} record of id {incident_id} doesn't exist"
        }), 400
    else:
        response = jsonify({
            "data": incident_of_id,
            "status": 200
        }), 200
    return response
