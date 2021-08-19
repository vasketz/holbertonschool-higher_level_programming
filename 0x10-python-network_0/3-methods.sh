#!/bin/bash
# write a script that takes a url and display all http methods
curl -s -I "$1" | grep Allow | cut -d" " -f2-
