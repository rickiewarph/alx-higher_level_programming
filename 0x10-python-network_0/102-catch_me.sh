#!/bin/bash
# script to make a request to 0.0.0.0:5000/catch_me that makes the server to respond with a message with You got me!, in the body of the response
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
