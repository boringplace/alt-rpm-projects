#!/usr/bin/python3

import sys

def Hello():
    print ("argc = %d" % len(sys.argv))

    num = 0
    for arg in sys.argv:
        print("argv[%d] = %s" % (num, arg))
        num += 1

if __name__ == "__main__":
    Hello()
