#!/bin/bash
# script to take in a URL, send a POST request to the passed URL, & display the body of the response
curl -sX POST $1 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -L
