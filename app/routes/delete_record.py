from flask import Blueprint, jsonify, request
from datetime import datetime
from app.models.incident import Incident

from app.helpers.authetication import token_required, non_admin

from app.helpers.validators import valid_url_input, set_incident_type

delete_record = Blueprint("delete_record", __name__, url_prefix="/api/v1")

response = None


@delete_record.route(
    "/<string:incident_type>/<int:incident_id>", methods=["DELETE"])
@token_required
@non_admin
def delete_red_flag_of_given_user(incident_id, incident_type):
    """Delete record with ID(incident_id) of a certain user"""
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
        incident_editable = Incident.incident_editable(incident_id, _type)
        if not incident_editable:
            response = jsonify({
                "status": 400,
                "error": f"Only {_type} in draft state can be deleted"
            }), 400
        else:
            Incident.delete_incident(incident_id, _type)
            response = jsonify({
                "status": 200,
                "data": [{
                    "id": incident_id,
                    "message": f"{_type} record has been deleted"
                }]}), 200
    return response
