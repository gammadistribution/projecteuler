"""Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
from util import integers


def main():
    INTEGER = 600851475143

    factors = integers.prime_factors(INTEGER)

    return factors[-1]
