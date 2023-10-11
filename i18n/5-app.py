#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale():
    """Select best match for locale."""
    # Check locale parameter present
    locale_from_url = request.args.get("locale")
    if locale_from_url and locale_from_url in app.config['LANGUAGES']:
        return locale_from_url

    # Fall back to default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """Returns user dictionary or None"""
    user_id = request.args.get("login_as")
    if user_id is not None:
        user = users.get(int(user_id))
        return user
    return None


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Route for index page """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
