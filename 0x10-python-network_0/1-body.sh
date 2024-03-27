#!/bin/bash
# script to take in a URL, send a request to that URL, and display the size of the body of the response
curl -sX GET $1 -L
