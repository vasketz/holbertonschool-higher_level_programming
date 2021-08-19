#!/bin/bash
# Write a script that takes an url, send a request and
curl -s "$1" -I | grep Content-Length | cut -d" " -f2
