#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_b = tuple_b + (0, 0)
    new_tuple = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return new_tuple
