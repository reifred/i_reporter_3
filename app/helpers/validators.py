import re
from flask import jsonify


def valid_url_input(incident_type):
    """ Validate urls """
    if incident_type not in ["red_flags", "interventions"]:
        return False
    _type = incident_type
    return True


def valid_patch_url(incident_type, incident_attr):
    """ Validate patch urls """
    if incident_attr not in ["location", "comment"]:
        return False
    return valid_url_input(incident_type)


def set_incident_type(incident_type):
    """ Set _type according to url input """
    if incident_type == "red_flags":
        _type = "red-flag"
    elif incident_type == "interventions":
        _type = "intervention"
    return _type


def validate_string(string_key, string_value):
    """ Validate the string """
    if not string_value or not isinstance(
            string_value, str) or string_value.isspace():
        return f"{string_key} should not be empty string"


def validate_media(media_key, media_value):
    """ Validate incident media """
    if not isinstance(media_value, list):
        return f"{media_key} should be in list form"


def validate_comment(comment):
    """ Validate incident comment """
    if not comment or not isinstance(
            comment, str) or comment.isspace():
        return "comment must not be empty string"
    if len(comment) not in range(10, 40):
        return "comment must be atleast 10 to 40 characters"


def validate_input(location, comment, images, videos):
    """ Validate incident input """
    error = {}
    error["location"] = validate_string("location", location)
    error["comment"] = validate_comment(comment)
    error["images"] = validate_media("images", images)
    error["videos"] = validate_media("videos", videos)
    error_list = [value for key, value in error.items() if value]
    first_error = "".join(error_list[0]) if error_list else None
    return first_error if len(error_list) == 1 else error_list


def validate_status(status):
    """ Validate incident status """
    if not status or not isinstance(status, str) or status.isspace():
        return "status must not be empty string"
    elif status not in ["resolved", "under investigation", "rejected"]:
        return "given status not allowed"


def validate_email(email):
    """ Validate user email """
    if not email or not isinstance(
            email, str) or email.isspace():
        return "email shoud not be empty string"
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "invalid email syntax"


def validate_password(password):
    """ Validate user password """
    if not password or not isinstance(
            password, str) or password.isspace():
        return "password shoud not be empty string"
    elif len(password) not in range(6, 16):
        return "password length should be between 6 to 16"
    elif(
        not re.search("[A-Z]", password) or
        not re.search("[a-z]", password) or
            not re.search("[0-9]", password)):
        return "password must have upper and lower character plus number"


def validate_phoneNumber(string_key, phoneNumber):
    """ Validate phone number """
    if not phoneNumber or not isinstance(
            phoneNumber, str) or phoneNumber.isspace():
        return f"{string_key} must not be empty string"
    if len(phoneNumber) not in range(10, 15):
        return f"{string_key} length must be 10 to 15 numbers"
    if not phoneNumber.isdigit():
        return f"{string_key} must have digits in a string"


def validate_name(string_key, name):
    if not name or not isinstance(
            name, str) or name.isspace():
        return f"{string_key} should not be empty string"
    if not name.isalpha():
        return f"{string_key} should contain only characters"


def validate_user_input(
        firstname, lastname, email, phoneNumber, username, password):
    """ Validate user data for sign up """
    error = {}
    error["firstname"] = validate_name("firstname", firstname)
    error["lastname"] = validate_name("lastname", lastname)
    error["email"] = validate_email(email)
    error["phoneNumber"] = validate_phoneNumber("phoneNumber", phoneNumber)
    error["username"] = validate_string("username", username)
    error["password"] = validate_password(password)
    error_list = [value for key, value in error.items() if value]
    first_error = "".join(error_list[0]) if error_list else None
    return first_error if len(error_list) == 1 else error_list


def validate_sign_in(username, password):
    """ Validate user data for login """
    error = {}
    error["username"] = validate_string("username", username)
    error["password"] = validate_password(password)
    error_list = [value for key, value in error.items() if value]
    first_error = "".join(error_list[0]) if error_list else None
    return first_error if len(error_list) == 1 else error_list
