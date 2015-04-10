"""Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""
import itertools


class Indexable(object):
    """Object to make an iterable indexable, i.e. return slice of iterable.
    """
    def __init__(self, it):
        self.it = iter(it)

    def __iter__(self):
        for elt in self.it:
            yield elt

    def __getitem__(self, index):
        try:
            return next(itertools.islice(self.it,
                                         index,
                                         index+1))
        except TypeError:
            return list(itertools.islice(self.it,
                                         index.start,
                                         index.stop,
                                         index.step))


def main():
    POSITION = 1000000
    LIMIT = 9

    permutations = Indexable(itertools.permutations(range(LIMIT + 1)))

    # The nth element of the list is n - 1.
    answer = "".join(map(str, permutations[POSITION - 1]))

    return answer
