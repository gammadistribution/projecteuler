import numpy as np


def find_neighborhood(matrix, origin, radius=4):
    """Find the neighborhood around the passed origin of the passed np.array,
    matrix. The variable origin is a 2-tuple consisting of a row index and
    a column index. This function finds the neighborhood of the passed radius
    around that row index, column index tuple. In this sense, the neighborhood
    of a radius, r, is the set of all (r - 1) adjacent elements,
    orthogonally and diagonally, to the origin. There are (r - 1) adjacent
    elements in the neighborhood as we are dealing with the discrete case in
    which the origin is included in the neighborhood. The indexes gathered for
    the neighborhood must all be positive and within the bounds of the matrix
    shape so as not to wrap around the matrix.

    Move in eight cardinal directions, orthogonally and diagonally away from
    origin. Use numpy arrays as unit vectors representing these directions
    which are stored in util.mathematics.settings.matrices_settings in the
    variable directions. Extend outward from origin by multiplying each unit
    vector by increasing magnitude to attempt to get all indexes within
    passed radius. Only collect groups that have a number of adjacent elements
    in a given number direction plus origin equal to passed radius.

    Returns list of groups of indexes used to access matrix values.
    """
    rows, cols = matrix.shape

    neighborhood = []
    for direction in get_unit_vectors():
        group = [origin]
        for magnitude in range(1, radius):
            direction_vector = magnitude * direction
            index = np.array(origin) + direction_vector
            x_dir, y_dir = index
            # If row index and column index are within bounds, i.e. do not
            # wrap around matrix, add to group.
            if 0 <= x_dir < rows and 0 <= y_dir < cols:
                group.append(tuple(index))
        # If the number of adjacent elements in a given direction plus origin
        # is equal to radius, add to neighborhood.
        if len(group) == radius:
            neighborhood.append(group)

    return neighborhood


def get_unit_vectors():
    """Get unit vectors representing eight cardinal directions. Iterate through
    integers in [-1, 1] for x position and integers in [-1, 1] for y position
    to create unit vectors as numpy.arrays, ignoring vector np.array((0, 0)).
    """
    directions = []
    for x_pos in range(-1, 1 + 1):
        for y_pos in range(-1, 1 + 1):
            if x_pos or y_pos:
                directions.append(np.array((x_pos, y_pos)))

    return directions
