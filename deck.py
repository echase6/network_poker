""""The Deck class for the network poker game, stores a deck of cards as a list of 52 card instances.

generate_deck() creates an instance of Deck with the 52 standard playing cards.
shuffle_the_deck() randomizes the order of the deck in place.
draw_card_from_deck() pulls the last card in the list of cards.
"""


from card import Card
from random import shuffle


class Deck:
    """Deck Class"""
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
    """Creates a list of all 52 cards and places them into an instance of Deck.

    >>> generate_deck(['H', 'D'], ['1', '2', '3'])
    Deck([Card('H', '1'), Card('H', '2'), Card('H', '3'), Card('D', '1'), Card('D', '2'), Card('D', '3')])
    """
    new_list = []
    for suit in suits:
        for rank in ranks:
            new_list += [Card(suit, rank)]
    return Deck(new_list)


def shuffle_the_deck(deck):
    """Uses the shuffle function from the random library to shuffle the list of cards in the Deck instance."""
    shuffle(deck.cards)


def draw_card_from_deck(deck):
    """Uses the pop function to remove a card from the deck and returns it. The pop function pulls from the end of the
    list of cards contained in a Deck instance."""
    return deck.cards.pop()
