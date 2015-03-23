"""Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from util import integers


def main():
    UPPER_BOUND = 2000000

    answer = sum([n for n in range(2, UPPER_BOUND) if integers.primality(n)])

    return answer
