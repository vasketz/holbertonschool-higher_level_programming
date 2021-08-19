#!/bin/bash
# write a script that takes a url and send a header with value
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
