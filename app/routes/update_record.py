from flask import Blueprint, jsonify, request
from datetime import datetime
from app.models.incident import Incident

from app.helpers.validators import (
    validate_string, validate_comment,
    valid_patch_url, set_incident_type
)

from app.helpers.authetication import (
    token_required,
    non_admin,
    json_data_required
)

update_record = Blueprint("update_record", __name__, url_prefix="/api/v1")

response = None


@update_record.route(
    "/<string:incident_type>/<int:incident_id>/<string:what_to_edit>",
    methods=["PATCH"])
@token_required
@non_admin
@json_data_required
def patch_red_flag_of_given_user(incident_type, incident_id, what_to_edit):
    """Update incident with ID(incident_id) of a certain user"""
    if not valid_patch_url(incident_type, what_to_edit):
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
        incident_editable = Incident.incident_editable(incident_id, _type)
        if not incident_editable:
            response = jsonify({
                "status": 400,
                "error": f"Only {_type} in draft state can be edited"
            }), 400
        else:
            comment = request.get_json().get("comment")
            location = request.get_json().get("location")
            data = location if what_to_edit == "location" else comment
            error = validate_string("location", data) \
                if what_to_edit == "location" else validate_comment(comment)

            if error:
                response = jsonify({"status": 400, "error": error}), 400
            else:
                Incident.update_incident(
                    what_to_edit, data, incident_id, _type)
                response = jsonify({
                    "status": 200,
                    "data": [{
                        "id": incident_id,
                        "message": f"Updated {_type} {what_to_edit}"
                    }]}), 200
    return response
