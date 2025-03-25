import flask


# TODO: change this to your academic email
AUTHOR = "myronk@sas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # FIXME: to be implemented
    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "Too short"}), 200
    if pw.islower():
        return flask.jsonify({"valid": False, "reason": "No uppercase letters"}), 200

    uppercase = 0
    digit = 0
    special = False
    for i in pw:
        if i.isupper():
            uppercase += 1
        if i.isnumeric():
            digit += 1
        if i in "!@#$%^&*":
            special = True
    if special == False:
        return flask.jsonify({"valid": False, "reason": "No special characters"}), 200
    if uppercase < 2:
        return flask.jsonify({"valid": False, "reason": "Not enough uppercase letters"}), 200
    if digit < 2:
        return flask.jsonify({"valid": False, "reason": "Not enough digits"}), 200
    
    
    return flask.jsonify({"valid": True, "reason": "Valid Password"}), 400
