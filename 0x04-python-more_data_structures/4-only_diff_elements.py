#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    i = 0
    l1 = list(i for i in set_1 if i not in set_2)
    l2 = list(i for i in set_2 if i not in set_1)
    lists = l1 + l2
    return lists
