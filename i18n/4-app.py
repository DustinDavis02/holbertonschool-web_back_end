#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template, request
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


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Route for index page """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
