#!/usr/bin/env python3

"""A module that will implement the dis function on a function"""

import dis

def fizzbuzz(num: int = 0):
    if (num == 15):
        print("fizzbuzz")
    elif (num == 5):
        print("fizz")
    elif (num == 3):
        print("buzz")
    else:
        print("{:d}".format(num))

if __name__ == "__main__":
    dis.dis(fizzbuzz)
