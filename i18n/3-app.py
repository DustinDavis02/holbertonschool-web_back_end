#!/usr/bin/env python3
"""Parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel, _, force_locale


class Config:
    """Configuration class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Main route"""
    best_match = request.accept_languages.best_match(["en", "fr"])
    with force_locale(best_match):
        return render_template('3-index.html', home_title=_("home_title"), home_header=_("home_header"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
