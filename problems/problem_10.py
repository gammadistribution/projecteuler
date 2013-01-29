#!/usr/bin/python


"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


import os
import sys
sys.path.append(os.path.join(os.path.split(os.getcwd())[0], 'modules'))

import integers


def main():
    UPPER_BOUND = 2000000

    answer = sum([n for n in range(2, UPPER_BOUND) if integers.primality(n)])

    print answer


if __name__ == "__main__":
    main()
