#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    lenght = (len(sys.argv) - 1)
    if lenght != 3 or lenght == 0:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif sys.argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif sys.argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif sys.argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Error")
        exit(1)
