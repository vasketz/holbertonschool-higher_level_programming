#!/usr/bin/python3
def uppercase(str):
    i = 0
    c = ''
    while len(str) > i:
        if str[i] >= 'a' and str[i] <= 'z':
            c += chr(ord(str[i]) - 32)
        else:
            c += chr(ord(str[i]))
        i += 1
    print("", c)  
