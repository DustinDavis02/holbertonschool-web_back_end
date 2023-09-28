#!/usr/bin/env python3
"""
This module sets up a basic Flask app with a single GET route.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    """
    GET route that returns a JSON welcome message.
    """
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
