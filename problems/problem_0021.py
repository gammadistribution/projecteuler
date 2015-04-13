"""Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import itertools
from util.mathematics import integers


def main():
    LIMIT = 10000

    divisors_sum = {number: sum(integers.proper_divisors(number))
                    for number in range(2, LIMIT + 1)}

    amicable_numbers = []
    for n1, n2 in itertools.product(divisors_sum, divisors_sum):
        # if the sum of proper divisors of n_1 is the same as n_2 and vice
        # versa, then n_1 is an amicable number.
        if divisors_sum[n1] == n2 and divisors_sum[n2] == n1 and n1 != n2:
            amicable_numbers.append(n1)

    answer = sum(amicable_numbers)

    return answer
