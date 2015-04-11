"""Problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""
import itertools
from util.mathematics import integers


def main():
    # Lowest abundant number is 12
    # Every number greater than 28123 can be written as the sum of two abundant
    # numbers so only need to check up to 28123.
    LOWERBOUND = 12
    UPPERBOUND = 28123

    abundant_numbers = [number for number in range(LOWERBOUND, UPPERBOUND + 1)
                        if sum(integers.proper_divisors(number)) > number]

    # Get the cross product of abundant numbers so we can determine every
    # number less than 28123 that is a sum of two abundant numbers.
    cross_product = itertools.product(abundant_numbers, abundant_numbers)

    sum_of_abundants = set((sum(tup) for tup in cross_product if
                            sum(tup) <= UPPERBOUND))

    # Every number less than or equal to UPPERBOUND that is not a part of the
    # set sum_of_abundants is the set we need.
    not_sum_of_abundants = set(range(1, UPPERBOUND + 1)) - sum_of_abundants

    answer = sum(not_sum_of_abundants)

    return answer
