#!/usr/bin/python3
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
    for j in numbers:
        if i < j and (i * 10) + j < 89:
            print("{:d}{:d}, ".format(i, j), end='')
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
