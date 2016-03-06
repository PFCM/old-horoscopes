"""
This module defines handlers/view functions for actually serving web pages.
"""

from flask import render_template, url_for
from flask import Flask

APP = Flask(__name__)


@APP.route('/')
def hello():
    """
    Serves the front page.
    """
    return render_template('hello.html',
                           horoscope_url=url_for('/_horoscope.json'),
                           starsign_url=url_for('/_starsign.json'))


@APP.route('/_horoscope.json')
def get_horoscope():
    """
    Fetches a horoscope from someone else and returns it.

    Parameters:
        sign (str): the star sign the horoscope is for.
        date (YYYY-MM-DD): the date to find a horoscope for.
    """
    pass


@APP.route('/_starsign.json')
def get_starsign():
    """
    Gets someone's star sign.

    Parameters:
        date (YYYY-MM-DD): the date of the person's birth.
    """
    pass


if __name__ == '__main__':
    APP.run(host='0.0.0.0')
