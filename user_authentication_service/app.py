#!/usr/bin/env python3
"""
This module sets up a basic Flask app with user registration and login.
"""

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome():
    """
    GET route that returns a JSON welcome message.
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'])
def users():
    """
    POST route for registering users.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def sessions():
    """
    POST route for logging in users.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response, 200
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """
    DELETE route for logging out users.
    """
    # session ID from cookies
    session_id = request.cookies.get('session_id')

    # Find user with given session ID
    user = AUTH.get_user_from_session_id(session_id)

    if user is not None:
        # Destroy session and redirect to GET /
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        # Respond with 403 HTTP status
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """
    GET route to fetch the user profile information.
    """
    # session ID from cookies
    session_id = request.cookies.get('session_id')

    # Find user with given session ID
    user = AUTH.get_user_from_session_id(session_id)

    if user is not None:
        # Respond with 200 and user's email
        return jsonify({"email": user.email}), 200
    else:
        # Respond with 403 HTTP status
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """ Generate reset password token """
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify(email=email, reset_token=reset_token), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """ Update user password """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        user = AUTH._db.find_user_by(email=email)
    except Exception:
        abort(403)

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
