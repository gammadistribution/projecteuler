"""Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""
number_map = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


BASE = 10


def number_to_words(number, british='and'):
    """Convert integer number into string of words. Map each digit in each
    place through number_map. Returns concatenated string of words for each
    number.
    """
    assert 1 <= number < 10000, "Number must be between 1 and 10,000."

    words = []

    number_string = str(number)
    for position in range(len(number_string)):
        digit_place = BASE ** position
        next_digit_place = BASE ** (position + 1)
        expanded_digit = number % next_digit_place - number % digit_place
        digit = expanded_digit / digit_place
        # ones place
        if not position:
            word = number_map[digit]
        # tens place
        elif position == 1:
            # If tens digit is one, use number_map on tens + ones digit
            if expanded_digit == BASE:
                last_two_digits = int(number_string[-2:])
                # Remove ones digit if tens digit is 1.
                word = number_map[last_two_digits]
                try:
                    words.pop()
                except IndexError:
                    pass
            else:
                word = number_map[expanded_digit]
        # hundreds place
        elif position == 2:
            word_list = [number_map[digit], number_map[digit_place]]
            if british:
                # if tens and one place are both not zero add british word
                if int(number_string[-position:]):
                    word_list.append(british)
            word = ' '.join(word_list)
        else:
            # If hundreds place is empty, remove word added for hundreds.
            if not int(number_string[-position]):
                words.pop()
            word_list = [number_map[digit], number_map[digit_place]]
            word = ' '.join(word_list)

        if word:
            words.append(word)

    # We move from ones place upwards so we have to reverse list of words to
    # have them appear in correct order.
    words.reverse()

    words = ' '.join(words)

    return words


def main():
    LIMIT = 1000

    words = []
    for number in range(1, LIMIT + 1):
        word = number_to_words(number)
        # Problem said to exclude spaces from counts.
        word = word.replace(' ', '')
        words.append(word)

    # Number of letters used in words is sum of each word's length.
    answer = sum(map(len, words))

    return answer
