"""Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def digit_summation(n):
    """The variable n is a positive integer.

    This function returns the sum of the number's digits.  For example,
    digit_summation(1234) would return 10, since 1 + 2 + 3 + 4 = 10.
    The function does this by turning the integer n to a string and applying
    sum to the iterator returned from mapping int to the string.
    """
    assert n == int(n), "Input is not an integer."
    assert n > 0, "Input is not a positive integer."

    return sum(map(int, str(n)))


def main():
    number = 2 ** 1000

    answer = digit_summation(number)

    return answer
