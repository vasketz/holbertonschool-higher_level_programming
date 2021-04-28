#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    hidden = dir(hidden_4)
    for i in range(0, len(hidden)):
        if hidden[i][0] != '_':
            print(hidden[i])
