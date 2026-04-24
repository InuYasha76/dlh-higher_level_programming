#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    count = len(argv)
    if count == 0:
        print("{:d} arguments.".format(count))
    elif count == 1:
        print("{:d} argument:".format(count))
    else:
        print("{:d} arguments:".format(count))
    for i, arg in enumerate(argv, start=1):
        print("{:d}: {:s}".format(i, arg))
