#!/usr/bin/python3
"""
script taking in a URL, sending a request to the URL and displaying 
value of the X-Request-Id variable found in header of the
response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """takes in a URL..."""
    with urllib.request.urlopen(argv[1]) as response:
        html_id = response.info().get('X-Request-Id')
        print(html_id)
