"""
Problem 4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from util.mathematics import integers


def main():
    # The smallest three digit number is 100 and the greatest three digit
    # number is 999, but we use 1000 so the use of range is easier.
    LOWER_BOUND = 100
    UPPER_BOUND = 1000

    largest = 0
    for x in range(LOWER_BOUND, UPPER_BOUND):
        for y in range(LOWER_BOUND, x):
            if integers.palindrome(x * y) and x * y > largest:
                largest = x * y

    answer = largest

    return answer
