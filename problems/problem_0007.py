#!/usr/bin/python


"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10 001st prime number?
"""


import os
import sys
sys.path.append(os.path.join(os.path.split(os.getcwd())[0], 'modules'))

import integers


def main():
    UPPER_BOUND = 10001

    primes = integers.primes(UPPER_BOUND)

    answer = primes[-1]

    print answer


if __name__ == "__main__":
    main()
