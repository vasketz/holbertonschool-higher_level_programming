#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenght = (len(sys.argv) - 1)
    args = sys.argv
    if lenght == 0: 
        print("0 arguments.")
    elif lenght == 1:
        print("1 argument:")
        print("1: {:s}".format(args[1]))
    elif lenght > 1:
        print("{:d} arguments:".format(lenght))
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, args[i]))
