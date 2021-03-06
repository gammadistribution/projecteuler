"""Problem 8

Find the greatest product of five consecutive digits in the 1000-digit number.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""
import os
import re


class NotStripped(Exception):
    pass


def get_path_variables():
    """Return the module's parent_directory and module name stripped of
    extension.
    """
    parent_directory = os.path.dirname(os.path.realpath(__file__))
    directory, filename = os.path.split(__file__)
    base, extension = os.path.splitext(filename)

    return parent_directory, base


def product(integers):
    """The variable integers is a list of integers.

    This function finds the product of every integer contained in integers
    and returns the product.  Function returns 0 if there is a 0 present in
    list without computing the product.
    """
    if 0 in integers:
        return 0

    product = integers.pop()

    for integer in integers:
        product *= integer

    return product


def product_finder(string, con_digits):
    """The variable string is a string representing an integer.  The variable
    con_digits is the number of consecutive digits to search for the product.

    This function finds the largest product of con_digits consecutive digits
    and returns the maximal product.
    """

    if re.search(" ", string) or re.search("\n", string):
        msg = "Input contains spaces or new line characters.  Exiting"
        raise NotStripped(msg)

    length = len(string)
    products = []

    for i, integer in enumerate(string):

        gap = i + con_digits

        if gap <= length:
            integers = string[i: gap]
            integers = [int(s) for s in integers]
            products.append(product(integers))

    return max(products)


def main():
    parent_directory, base = get_path_variables()

    path = os.path.join(parent_directory, 'input', base, 'number.txt')

    with open(path) as f:
        lines = f.readlines()
        string = "".join([s.replace(" ", "").replace("\n", "") for s in lines])

    try:
        answer = product_finder(string, 5)
    except NotStripped:
        answer = None

    return answer
