"""Problem 25

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""


def main():
    LIMIT = 1000

    a, b = 1, 1
    position = 1

    # Find the position of the first term of Fibonacci to contain LIMIT digits.
    while len(str(a)) < LIMIT:
        a, b = a + b, a
        position += 1

    # The last position is the position for the term strictly less than LIMIT.
    position += 1

    return position
