#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    result = []
    for i in my_list:
        if i not in result:
            result.append(i)
            suma += i
    return suma
