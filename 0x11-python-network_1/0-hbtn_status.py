#!/usr/bin/python3
"""script to fetch https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    """fetching https://intranet.hbtn.io/status"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        html_str = html.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html_str))
