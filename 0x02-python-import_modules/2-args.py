#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i <= 1:
        print("0 arguments.")
    elif i == 2:
        print("{} argument:".format(i - 1))
    else:
        print("{} arguments:".format(i - 1))
    for i in range(len(sys.argv) - 1):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
