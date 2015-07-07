import math
import numpy as np


def create_spiral(array, starting_position, radius):
    """With this function, we hope to create the current outermost spiral
    for the given array. The array is a numpy array of size n x n. The
    starting_position is a tuple representing the position of the midpoint of
    the array, e.g. if we have an array of size 7 x 7, then
    starting_position = (3, 3).

    The passed radius corresponds to the number of spirals in the array from
    the midpoint, e.g. radius 3 corresponds to 3 spirals from the midpoint. For
    an array of size 7 x 7, that corresponds to the outermost spiral of the
    array. The following indicates the spirals for an array of size 7 x 7:

    3 3 3 3 3 3 3
    3 2 2 2 2 2 3
    3 2 1 1 1 2 3
    3 2 1 0 1 2 3
    3 2 1 1 1 2 3
    3 2 2 2 2 2 3
    3 3 3 3 3 3 3

    We create the spiral for the passed array by starting at the top right
    corner of the square the spiral forms move down 1 and then move downward
    (0), leftward (1), upward(2), and rightward (3) until we meet where we
    began. The diagram below illustrates the traversal we take for spiral of
    radius 3.

    2 3 3 3 3 3 3
    2 x x x x x 0
    2 x x x x x 0
    2 x x x x x 0
    2 x x x x x 0
    2 x x x x x 0
    1 1 1 1 1 1 0

    The length of one side of the square that we are spiraling is 2 * radius
    so that we do not overlap sides. The goal is to start at the top right
    corner and traverse the square in the direction provided, incrementing the
    number assigned to the array each step of the way. So the final spiral
    array for radius 3 would look like the following:

    43 44 45 46 47 48 49
    42 xx xx xx xx xx 26
    41 xx xx xx xx xx 27
    40 xx xx xx xx xx 28
    39 xx xx xx xx xx 29
    38 xx xx xx xx xx 30
    37 36 35 34 33 32 31

    where the x's would have been populated previously.

    Updates the array as described for the spiral corresponding to the passed
    radius.
    """
    # Initialize row, col to start at top right corner of current spiral.
    row, col = starting_position[0] - radius, starting_position[1] + radius

    # The spiral numbers for a given radius r start at ((2r - 1) ^ 2) + 1 and
    # end at (2r + 1) ^ 2
    begin = ((2 * radius) - 1) ** 2 + 1
    end = ((2 * radius) + 1) ** 2 + 1

    increment = int((end - begin) / 4)

    # Four sides in a square, four directions we must traverse.
    for side in range(4):
        # Each segment of the square corresponds to a certain direction we must
        # travel in order to create the spiral, e.g. 0 is the first side of the
        # square we encounter and in order to make the spiral we must go down,
        # i.e. keeping the column element the same and increasing the row
        # element.
        directions = return_directions(side)

        for element in range(begin + side * increment,
                             begin + (side + 1) * increment):
            row += directions['row']
            col += directions['col']
            array[row][col] = element


def initialize_array(size, starting_element=1):
    """Create a numpy array with the number of rows and columns equal to size.
    Find the midpoint of the array given by the position indicated by
    the (size / 2, size / 2) rounded down. Initialize the position of the array
    at that midpoint to be the starting_element.
    """
    midpoint = math.floor(size / 2)

    array = np.empty((size, size), dtype=np.int)

    array[midpoint][midpoint] = starting_element

    return array


def populate_array(array, size):
    """Given an initialized array of given size, create x spirals for the array
    where x = size / 2 rounded down.

    Return the array with the added spirals.
    """
    midpoint = math.floor(size / 2)
    starting_position = (midpoint, midpoint)

    for radius in range(1, midpoint + 1):
        create_spiral(array, starting_position, radius)

    return array


def return_directions(side):
    """Return the row and col incrementers for the passed side of the
    rectangle.
    """
    directions = {
        0: {
            'row': 1,
            'col': 0
        },
        1: {
            'row': 0,
            'col': -1
        },
        2: {
            'row': -1,
            'col': 0
        },
        3: {
            'row': 0,
            'col': 1
        }
    }

    return directions[side]


def sum_diagonals(array, size):
    """Sum the diagonals of the passed array. Subtract out the intersection
    of the two diagonals, the midpoint of the array.
    """
    diagonal = array.diagonal(0)
    reverse_diagonal = np.flipud(array).diagonal(0)[::-1]

    midpoint = array[math.floor(size / 2)][math.floor(size / 2)]

    return sum(diagonal) + sum(reverse_diagonal) - midpoint


def main():
    SIZE = 1001

    assert SIZE % 2 == 1, "SIZE must be odd."

    array = initialize_array(SIZE)

    array = populate_array(array, SIZE)

    answer = sum_diagonals(array, SIZE)

    return answer
