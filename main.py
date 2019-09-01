"""Module to work with URLs via 'bitly.com'."""
import requests
import os
from dotenv import load_dotenv
import argparse


def shorten_link(token, link):
    """
    Method to reduce by specify URL.

    :param token: Generic Access Token from 'bitly.com'.
    :param link: Required link.

    :returns: Dict with data for shorten URL.
    """
    if link.startswith('http://') or link.startswith('https://'):
        wrapped_url = dict(long_url=link)
    else:
        wrapped_url = dict(long_url='https://{0}'.format(link))

    auth_header = dict(Authorization='Bearer {0}'.format(token))
    response = requests.post('https://api-ssl.bitly.com/v4/shorten',
                             headers=auth_header,
                             json=wrapped_url)
    response.raise_for_status()
    return response.json()


def count_clicks(token, link):
    """
    Method to counting the number of clicks by specify shorten URL.

    :param token: Generic Access Token from 'bitly.com'.
    :param link: Required link.

    :returns: Count click for shorten URL.
    """
    data_settings = dict(unit='month', units='-1')
    auth_header = dict(Authorization='Bearer {0}'.format(token))
    response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/{0}/clicks/summary'.format(link),
                            headers=auth_header,
                            params=data_settings)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    load_dotenv()
    BITLY_ACCESS_TOKEN = os.getenv("BITLY_ACCESS_TOKEN")

    parser = argparse.ArgumentParser('Program description')
    parser.add_argument('specified_url', help='Link for reduce or get count clicks for "bit.ly"')
    args = parser.parse_args()
    specified_url = args.specified_url

    try:
        if specified_url.startswith('http://bit.ly/'):
            clicks_count = count_clicks(BITLY_ACCESS_TOKEN, specified_url[7:])
            print('Count clicks for "bit.ly" link: {0}'.format(clicks_count['total_clicks']))
        elif specified_url.startswith('bit.ly/'):
            clicks_count = count_clicks(BITLY_ACCESS_TOKEN, specified_url)
            print('Count clicks for "bit.ly" link: {0}'.format(clicks_count['total_clicks']))
        else:
            bitlink = shorten_link(BITLY_ACCESS_TOKEN, specified_url)
            print('Your link: {0}'.format(bitlink['link']))
    except requests.exceptions.HTTPError:
        raise ValueError('Sorry, entered BAD url! Try again ^)')
