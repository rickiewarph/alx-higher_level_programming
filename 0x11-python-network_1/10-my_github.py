#!/usr/bin/python3
"""
takes your Github credentials (username and password) and uses the
Github API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes your Github credentials ...
    """
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    rq = requests.get(url, auth=(rickiewarph, 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))
    try:
        print(rq.json().get('id'))
    except:
        pass
