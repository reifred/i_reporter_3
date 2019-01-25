from flask import Blueprint, jsonify, request
from datetime import datetime
from app.models.incident import Incident

from app.helpers.validators import (
    valid_url_input, set_incident_type, validate_status
)

from app.helpers.authetication import (
    token_required,
    admin_required,
    json_data_required
)

edit_status = Blueprint("edit_status", __name__, url_prefix="/api/v1")

response = None


@edit_status.route(
    "/<string:incident_type>/<int:incident_id>/status",
    methods=["PATCH"]
)
@token_required
@admin_required
@json_data_required
def edit_status_of_user_record(incident_type, incident_id):
    """Edit record status of ID(incident_id)"""
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
        status = request.get_json().get("status")
        error = validate_status(status)
        if error:
            response = jsonify({"status": 400, "error": error}), 400
        else:
            Incident.update_incident("status", status, incident_id, _type)
            response = jsonify({
                "status": 200,
                "data": [{
                    "id": incident_id,
                    "message": f"Updated {_type} status"
                }]}), 200
    return response
