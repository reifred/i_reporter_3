from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from app.routes.home import home
from app.routes.auth import auth_bp
from app.routes.get_records import get_records
from app.routes.get_specific_record import get_single_record
from app.routes.create_record import create_record
from app.routes.edit_record_status import edit_status
from app.routes.update_record import update_record
from app.routes.delete_record import delete_record
from app.routes.get_users import get_users

app = Flask(__name__)
CORS(app)
app.register_blueprint(home)
app.register_blueprint(create_record)
app.register_blueprint(get_records)
app.register_blueprint(get_single_record)
app.register_blueprint(edit_status)
app.register_blueprint(update_record)
app.register_blueprint(delete_record)
app.register_blueprint(get_users)
app.register_blueprint(auth_bp)


@app.errorhandler(Exception)
def errors(error):
    """
    This funcion handles the 404 and 405 HTTP STATUS CODES.
    It then returns json response on a particular status code.
    """
    response = None
    if error.code == 404:
        response = jsonify({
            "status": 404,
            "error": "Page Not found. Enter a valid URL"
        }), 404
    else:
        response = jsonify({
            "status": 405,
            "error": "Method not allowed."
        }), 405
    return response
