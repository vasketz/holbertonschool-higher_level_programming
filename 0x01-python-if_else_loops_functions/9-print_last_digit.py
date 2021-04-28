#!/usr/bin/pyhton3
def print_last_digit(number):
    ld = abs(number) % 10
    print("{:d}".format(ld), end='')
    return ld
