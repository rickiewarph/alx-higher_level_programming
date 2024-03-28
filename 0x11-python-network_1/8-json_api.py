#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a letter and ...
    """
    url = 'http://0.0.0.0:5000/search_user'
    rq = requests.get(url)
    if len(argv) == 2:
        rq = requests.post(url, data={'q': argv[1]})
    else:
        rq = requests.post(url, data={'q': ""})
    try:
        if rq.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(rq.json().get('id'), rq.json().get('name')))
    except:
        print("Not a valid JSON")
