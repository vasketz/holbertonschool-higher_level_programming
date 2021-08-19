#!/bin/bash
# Write a script that takes an url, send a request and
# display the size of the body
curl -s "$1" -I | grep Content-Lenght | cut -d" " -f2
