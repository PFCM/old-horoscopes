"""
This module defines handlers/view functions for actually serving web pages.
"""
import json
import re

import requests

from flask import render_template, url_for
from flask import Flask, request, Response

APP = Flask(__name__)

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']


@APP.route('/')
def hello():
    """
    Serves the front page.
    """
    return render_template('hello.html',
                           horoscope_url=url_for('get_horoscope'),
                           starsign_url=url_for('get_starsign'))


@APP.route('/_horoscope.json')
def get_horoscope():
    """
    Fetches a horoscope from someone else and returns it.

    Parameters:
        sign (str): the star sign the horoscope is for.
        date (YYYY-MM-DD): the date to find a horoscope for.

    Returns:
        JSON, looking like:

            {
                sign: star_sign,
                date: YYYY-MM-DD,
                horoscope: "text describing a horoscope"
            }
    """
    # grab the parameters
    sign = request.args['sign'].title()  # uppercase the first one
    year, month, day = request.args['date'].split('-')
    if len(day) == 2 and day[0] == '0':
        day = day[1]
    # construct the url
    # we steal these from a webpage so it's not crazy simple
    url_root = 'http://www.gotohoroscope.com'
    url_year = '/{}-horoscope'.format(year)
    url_day = '/{}{}.html'.format(day, MONTHS[int(month)])
    request_url = url_root + url_year + url_day
    # make the request
    response = requests.get(request_url)
    # now we have to find the sign we are after in this mess of a web page
    page_data = response.text  # do this once because it sometimes does stuff
    match = re.search('<u>'+sign+' Daily Horoscope.*/>(\n.*\n){1}',
                      page_data)
    if match:
        horoscope = match.group(1).strip()
    else:
        horoscope = 'Could not find a horoscope :('

    # and build the results dict
    results = {
        'sign': sign,
        'date': '-'.join([year, month, day]),
        'horoscope': horoscope
    }
    return Response(json.dumps(results),
                    mimetype='application/json')


@APP.route('/_starsign.json')
def get_starsign():
    """
    Gets someone's star sign. Steals the data from astroica.com

    Parameters:
        date (YYYY-MM-DD): the date of the person's birth.

    Returns:

        {
            sign: name of sign,
            stone: birth stone,
            flower: birth flower,
            planet: your planet,
            color: your color,
            element: your element
        }
    """
    year, month, day = request.args['date'].split('-')
    # make the url
    url = 'http://www.astroica.com/western-astrology/zodiac.php?'
    url += 'year={}&month={}&day={}&p=1'.format(year, month, day)
    # make the request
    response = requests.get(url)

    page_data = response.text
    # now find the table up the top and get the info out of it
    print(url)
    # print(page_data)
    sign = re.search('<tr><th>Zodiac Sign</th><td><strong>(.*)</strong>',
                     page_data).group(1).strip()
    stone = re.search('<tr><th>Birth Stone</th><td>(.*)</td>',
                      page_data).group(1).strip()
    flower = re.search('<tr><th>Birth Flower</th><td>(.*)</td>',
                       page_data).group(1).strip()
    planet = re.search('<tr><th>Planet</th><td>(.*)</td>',
                       page_data).group(1).strip()
    color = re.search('<tr><th>Color</th><td>(.*)</td>',
                      page_data).group(1).strip()
    element = re.search('<tr><th>Element</th><td>(.*)</td>',
                        page_data).group(1).strip()

    return Response(json.dumps({'sign': sign,
                                'stone': stone,
                                'flower': flower,
                                'planet': planet,
                                'color': color,
                                'element': element
                                }),
                    mimetype='application/json')


if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=True)
