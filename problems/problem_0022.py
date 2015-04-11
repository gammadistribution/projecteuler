"""Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
 obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""
import os


def get_path_variables():
    """Return the module's parent_directory and module name stripped of
    extension.
    """
    parent_directory = os.path.dirname(os.path.realpath(__file__))
    directory, filename = os.path.split(__file__)
    base, extension = os.path.splitext(filename)

    return parent_directory, base


def name_score(position, name, offset=64):
    """The name score of a given name in a list is the name's position in the
    list multiplied by the sum of the string's characters' values. For
    instance, if name is MATT and 2nd in list, the character's values would be
    13, 1, 20, and 20, the sum of which is 54. Therefore the name_score for
    MATT in that particular list would be 2 * 54 = 108. Since we work with
    zero-indexed lists, we will have to increase position by one. This also
    assumes the passed name is made up only of ASCII characters.
    """
    char_scores = [ord(character) - offset for character in name.upper()]

    return (position + 1) * sum(char_scores)


def sanitize_input(path):
    """Given path to input file, read in file and split text based off of
    comma delimiter. Replace each " with empty string. Sort resulting list
    of text.

    Returns sorted list.
    """
    with open(path) as f:
        names = f.read()
        names = names.split(',')
        names = [name.replace('"', '') for name in names]

    names.sort()

    return names


def main():
    parent_directory, base = get_path_variables()

    path = os.path.join(parent_directory, 'input', base, 'names.txt')

    names = sanitize_input(path)

    scores = [name_score(position, name)
              for position, name in enumerate(names)]

    answer = sum(scores)

    return answer
