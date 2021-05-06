#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    for i in matrix:
        aux_m = []
        for j in i:
            j = j ** 2
            aux_m.append(j)
        new_m.append(aux_m)
    return new_m
