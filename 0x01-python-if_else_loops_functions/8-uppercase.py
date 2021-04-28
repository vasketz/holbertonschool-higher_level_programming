#!/usr/bin/python3
def uppercase(str):
    c = ''
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            c += chr(ord(str[i]) - 32)
        else:
            c += chr(ord(str[i]))
    print("{:s}".format(c))
