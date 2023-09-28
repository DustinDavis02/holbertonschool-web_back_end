#!/usr/bin/env python3
"""
This module sets up a basic Flask app with user registration and login.
"""

from flask import Flask, jsonify, request, abort
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
