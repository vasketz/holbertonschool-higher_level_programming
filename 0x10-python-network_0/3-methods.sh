#!/bin/bash
# write a script that takes a url and display all http methods
curl -s -I nocseteipsum.tech | grep Allow | cut -d" " -f2
