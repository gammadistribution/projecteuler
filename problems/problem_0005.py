"""Problem 5

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
from util.mathematics import integers


def main():
    """The smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20 is the least common multiple of all such numbers.
    """
    # Get list of all numbers from 1 to 20.
    factors = list(range(21))[1:]

    answer = integers.lcm_multiple(factors)

    return answer


if __name__ == "__main__":
    main()
