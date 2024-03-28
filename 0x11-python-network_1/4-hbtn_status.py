#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status using requests"""
import requests


if __name__ == "__main__":
    """fetches https://intranet.hbtn.io/status using requests"""
    rq = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(rq.text)))
    print("\t- content: {}".format(rq.text))
