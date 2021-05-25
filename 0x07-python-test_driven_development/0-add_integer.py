#!/usr/bin/python3
"""
python3 -c 'print(__import__("0_add_integer").__doc__)'
"""

def add_integer(a, b=98):
    """return a + b
    python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)'
    """
    '''
    >>> add_integer(2 + 3)
    5
    '''
    if type(b) is float:
        b = int(b)
    if type(a) is float:
        a = int(a)
    if type(a) is int and type(b) is int:
        return a + b
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    
if __name__ == "__main__":
    import doctype
    doctest.testmod()
