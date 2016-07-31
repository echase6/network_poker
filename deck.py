""""Sets up the Deck class for a network Poker game"""


from card import Card
from random import shuffle


class Deck:
    def __init__(self, cards):
        self.cards = cards


    def __eq__(self, other):
        """Return eq
        >>> (
        ... Deck() ==
        ... Deck()
        ... )
        True
        >>> (
        ... Deck() ==
        ... Deck(1)
        ... )
        False
        """
        return(
            self.cards == other.cards
        )


    def __repr__(self):
        """Return repr.
        >>> repr(Deck([Card('H', '5'), Card('C', '2')]))
        "Deck([Card('H', '5'), Card('C', '2')])"
        """
        return 'Deck({!r})'.format(
            self.cards
        )


def generate_deck(suits, ranks):
    """create a list of Cards and save them to a Deck
    >>> generate_deck(['H', 'D'], ['1', '2', '3'])
    Deck([Card('H', '1'), Card('H', '2'), Card('H', '3'), Card('D', '1'), Card('D', '2'), Card('D', '3')])
    """
    new_list = []
    for suit in suits:
        for rank in ranks:
            new_list += [Card(suit, rank)]
    return Deck(new_list)


def shuffle_the_deck(deck):
    """relies on the random library shuffle function to reliably randomize the order of cards, does this in place"""
    shuffle(deck.cards)


def draw_card_from_deck(deck):
    """Removes a card from the deck to add to the players hand"""
    return deck.cards.pop()