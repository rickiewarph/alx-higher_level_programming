#!/bin/bash
# script to take in a URL as an argument, send a GET request to the URL, & display the body of the response
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
