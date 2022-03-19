#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""

from urllib.request import urlopen


def main():
    """ fetch python script"""
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8'
        .format(type(html), html),
        'content: {}'.format(html.decode('utf-8')))


if __name__ == "__main__":
    main()
