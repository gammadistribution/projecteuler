"""Problem 54

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives. But if two
ranks tie, for example, both players have a pair of queens, then highest cards
in each hand are compared (see example 4 below); if the highest cards tie then
the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
"""
from collections import Counter
import functools
import os


@functools.total_ordering
class PlayingCard(object):
    """Use this class to instantiate an object representing a playing card
    from a normal 52 card deck of playing cards used in games such as poker.
    """
    def __init__(self, card):
        self.card = card
        value, suit = card
        suit = suit.upper()

        assert value in self._mapping.keys(), 'Value of card not valid.'
        assert suit in ['C', 'D', 'H', 'S'], 'Suit of card not valid.'

        self.value = value
        self.suit = suit

    @property
    def _mapping(self):
        """Use this mapping to determine the value of a card. Note that the
        value 'A', or ace, may also be used as a low card, or 1, when checking
        for a straight. However, in all other instances it's beneficial to
        consider it a high card.
        """
        mapping = {str(number): number for number in range(2, 10)}
        mapping.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})

        return mapping

    def __eq__(self, other):
        """This PlayingCard is equal to other PlayingCard if this
        PlayingCard's suit and value are the same as other PlayingCard.
        Note that in a valid 52 playing card deck, there is only one of each
        card. Therefore, it is invalid to have two equal PlayingCards when
        using such a deck as you would in a game such as Poker."""
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other):
        """This PlayingCard is less than other PlayingCard if the
        value of the card is less than other using mapping defined
        by property PlayingCard._mapping and also if the character
        representing suit
        """
        tuple_1 = (self._mapping[self.value], self.suit)
        tuple_2 = (other._mapping[other.value], other.suit)

        return tuple_1 < tuple_2

    def __repr__(self):
        return "'{0}{1}'".format(self.value, self.suit)

    def __str__(self):
        return "{0}{1}".format(self.value, self.suit)


@functools.total_ordering
class PokerHand(object):
    """Use this class to instantiate a list of tuples to form a grouping of
    PlayingCards. cards is a string of two characters, value and suit, the
    card's value and suit.
    """
    def __init__(self, cards, number_of_cards=5):
        self.cards = sorted([PlayingCard(card) for card in cards])
        self.number_of_cards = number_of_cards
        msg = 'Passed list cards has different number of elements than {} '
        msg += ', the variable number_of_cards'
        assert len(self.cards) == number_of_cards, msg.format(number_of_cards)
        # If the hand is a straight and A is low card, rearrange list of cards.
        if self.straight and set(['A', '2']).issubset(self.values.keys()):
            ace = self.cards.pop()
            self.cards.insert(0, ace)

    @property
    def suits(self):
        """Return a dictionary containing the count of each suit in the list
        self.cards.
        """
        return Counter([card.suit for card in self.cards])

    @property
    def values(self):
        """Return a dictionary containing the count of each card value in the
        list self.cards.
        """
        return Counter([card.value for card in self.cards])

    @property
    def high_card(self):
        """The high card of a poker hand is the highest valued card in the
        hand. As self.cards is sorted according to value, then suit, the last
        element of the list is the high card of the instance of PokerHand.
        """
        return self.cards[-1]

    @property
    def straight(self):
        """Return True if the values of the PokerHand form a sequential list.
        Note that value 'A', or ace, can be used both as a high and low card,
        i.e. 'A' may take the value of 1 or 14 when determining a straight.
        """
        # Enumerate all possible straights using numberical mapping of card
        # values, i.e. [[1, 2, 3, 4, 5], ..., [10, 11, 12, 13, 14]] using
        # standard deck and hand sizes.
        possible_straights = [range(i, i + self.number_of_cards)
                              for i in range(1, 10 + 1)]
        sequence_high = [card._mapping[card.value] for card in self.cards]
        # Make aces low and check if sequence is found as well.
        sequence_low = sorted([card._mapping[card.value] if card.value != 'A'
                               else 1 for card in self.cards])
        condition_1 = sequence_high in possible_straights
        condition_2 = sequence_low in possible_straights

        return condition_1 or condition_2

    @property
    def royal(self):
        """A poker hand is royal if the values of the cards contain the highest
        possible values, i.e. T, J, Q, K, A.
        """
        return set(self.values.keys()) == set(['T', 'J', 'Q', 'K', 'A'])

    @property
    def flush(self):
        """Return True if the value number_of_cards is found in the values
        of the object's suits dictionary.
        """
        return self.number_of_cards in self.suits.values()

    def _strength_mapping(self, strength):
        """Convert the string values of a hand's strength to a numeric value
        for comparison purposes.
        """
        mapping = {
            'Royal Flush': 9,
            'Straight Flush': 8,
            'Four of a Kind': 7,
            'Full House': 6,
            'Flush': 5,
            'Straight': 4,
            'Three of a Kind': 3,
            'Two Pairs': 2,
            'One Pair': 1,
            'High Card': 0
            }

        return mapping[strength]

    @property
    def _strength(self):
        """The strength of a poker hand is the highest valued combination of
        cards in the hand. The highest to lowest poker hand strenghs are
        enumerated below:

        Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        Straight Flush: All cards are consecutive values of same suit.
        Four of a Kind: Four cards of the same value.
        Full House: Three of a kind and a pair.
        Flush: All cards of the same suit.
        Straight: All cards are consecutive values.
        Three of a Kind: Three cards of the same value.
        Two Pairs: Two different pairs.
        One Pair: Two cards of the same value.
        High Card: Highest value card.

        Returns the string and numerical value of the hand's strength, as well
        as the value of the high card of the hand for tie-breaking purposes.
        """
        values_set = sorted(self.values.values())
        high_card = self.high_card

        if self.royal and self.flush:
            strength = 'Royal Flush'
        elif self.straight and self.flush:
            strength = 'Straight Flush'
        elif [1, 4] == values_set:
            strength = 'Four of a Kind'
            high_card = max([card for card in self.cards
                             if self.values[card.value] == 4])
        elif [2, 3] == values_set:
            strength = 'Full House'
        elif self.flush:
            strength = 'Flush'
        elif self.straight:
            strength = 'Straight'
        elif [1, 1, 3] == values_set:
            strength = 'Three of a Kind'
            high_card = max([card for card in self.cards
                             if self.values[card.value] == 3])
        elif [1, 2, 2] == values_set:
            strength = 'Two Pairs'
            high_cards = []
            for key in self.values.keys():
                if self.values[key] == 2:
                    high_cards.append(max([card for card in self.cards
                                           if self.values[card.value] == 2]))
            high_card = max(high_cards)
        elif [1, 1, 1, 2] == values_set:
            strength = 'One Pair'
            high_card = max([card for card in self.cards
                             if self.values[card.value] == 2])
        else:
            strength = 'High Card'

        return (strength,
                self._strength_mapping(strength),
                high_card._mapping[high_card.value])

    @property
    def strength(self):
        """Returns the string value of the hand's strength. Uses internal
        method, self._strength to determine hand's strength.
        """
        return self._strength[0]

    def __eq__(self, other):
        """Two poker hands are equal if the strength of each hand is the same
        and the value of the high card is the same.
        """
        strength_string_1, strength_1, high_card_1 = self._strength
        strength_string_2, strength_2, high_card_2 = other._strength
        return strength_1 == strength_2 and high_card_1 == high_card_2

    def __lt__(self, other):
        """This poker hand is less than other poker hand if the strength value
        is lower than other strength value. If strengths are the same, this
        poker hand is less than other poker hand if high_card is lower.
        """
        strength_string_1, strength_1, high_card_1 = self._strength
        strength_string_2, strength_2, high_card_2 = other._strength

        condition_1 = strength_1 < strength_2
        condition_2 = (strength_1 == strength_2 and high_card_1 < high_card_2)

        return condition_1 or condition_2

    def __repr__(self):
        cards = ["'{0.value}{0.suit}'".format(card) for card in self.cards]
        return '[{0}]'.format(', '.join(cards))

    def __str__(self):
        cards = [''.join([card.value, card.suit]) for card in self.cards]
        return ' '.join(cards)


def get_hands(path):
    """Return the contents of the file found at path into a list with the
    new line character stripped.
    """
    with open(path) as f:
        rounds = [line.strip('\n') for line in f.readlines()]

    return rounds


def get_path_variables():
    """Return the module's parent_directory and module name stripped of
    extension.
    """
    parent_directory = os.path.dirname(os.path.realpath(__file__))
    directory, filename = os.path.split(__file__)
    base, extension = os.path.splitext(filename)

    return parent_directory, base


def separate_hands(rounds, delimiter=' ', number_of_cards=5):
    """Take a list of lists and split each inner list according to past
    delimiter. Then separate the split list into two parts,the first
    number_of_cards elements and every element after the first number_of_cards
    elements. Append to a list as a tuple the two separated lists with the
    first element of the tuple, the list with the first number_of_cards
    elements.
    """
    hands = []
    for cards in rounds:
        cards = cards.split(delimiter)
        hand_1 = PokerHand(cards[:number_of_cards])
        hand_2 = PokerHand(cards[number_of_cards:])
        hands.append((hand_1, hand_2))

    return hands
