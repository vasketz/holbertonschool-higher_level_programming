#!/bin/bash
# write a script that takes an url an send post request
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
