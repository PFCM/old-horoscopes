"""
This module defines handlers/view functions for actually serving web pages.
"""

from flask import render_template
from flask import Flask

APP = Flask(__name__)


@APP.route('/')
def hello():
    """
    Serves the front page.
    """
    return render_template('hello.html')


if __name__ == '__main__':
    APP.run(host='0.0.0.0')
