"""##NOT USED##


A class for storing the burn pile on the poker table, cards in it are stored in a list and not intended to be shown
during the course of the game"""

from card import Card
from deck import Deck

class Burn:
    def __init__(self, burn_pile):
        self.burn_pile = burn_pile

    def __eq__(self, other):
        """tests eq

        >>> Burn([]) == Burn([])
        True
        """
        return self.burn_pile == other.burn_pile

    def __repr__(self):
        """sets the repr for the Burn class

        >>> repr(Burn([Card('H', '5'), Card('C', '2')]))
        "Burn([Card('H', '5'), Card('C', '2')])"
        """
        return 'Burn({!r})'.format(
            self.burn_pile
        )
