#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
body of the response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL, and ...
    """
    url = argv[1]
    rq = requests.get(url)
    if rq.status_code >= 400:
        print("Error code: {}".format(rq.status_code))
    else:
        print(rq.text)
