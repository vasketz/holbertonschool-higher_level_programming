#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import add
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
from calculator_1 import sub
if __name__ == "__main__":
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
from calculator_1 import mul
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, mul(a, b)))
from calculator_1 import div
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, div(a, b)))
