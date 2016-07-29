"""sets up the Card class and functions for the Network Poker game"""

SUITS = ['H', 'D', 'C', 'S']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    """A class for representing a card in blackjack"""

    def __init__(self, suit, rank,):
        self.suit = suit
        self.rank = rank

    def __eq__(self, other):
        """

        >>> Card('A', 'H') == Card('A', 'H')
        True
        >>> Card('A', 'H') == Card('2', 'H')
        False
        """
        return(
            self.suit == other.suit and
            self.rank == other.rank
        )

    def __repr__(self):
        """

        >>> Card('H', 'K')
        Card('H', 'K')
        """
        return 'Card({!r}, {!r})'.format(
            self.suit,
            self.rank
        )