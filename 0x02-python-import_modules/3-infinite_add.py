#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    lenght = len(sys.argv)
    if lenght == 1:
        print("0")
    else:
        for i in range(1, lenght):
            result = result + int(sys.argv[i])
        print(result)
