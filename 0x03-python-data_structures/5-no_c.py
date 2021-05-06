#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for i in range(len(my_string)):
        s = my_string[i]
        if s == "c" or s == "C":
            s = ""
        new = new + s
    return new
