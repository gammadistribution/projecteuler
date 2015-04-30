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
