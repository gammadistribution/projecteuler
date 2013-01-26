#!/usr/bin/python

"""
Problem 6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^ 2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""


def main():
    UPPER_BOUND = 100
    
    sum_squares = sum([x ** 2 for x in range(UPPER_BOUND + 1)])
    
    square_sums = sum(range(UPPER_BOUND + 1)) ** 2

    answer = square_sums - sum_squares

    print answer


if __name__ == "__main__":
    main()
