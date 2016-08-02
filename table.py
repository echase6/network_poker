"""The Table class, which contains the players, the deck, a kitty and a pot.

Initializes to no players, and un-shuffled deck, and an pot with 0 value.
str() function renders the table (for the server only.)
"""

from player import Player
from pot import Pot
from deck import Deck
from card import Card


class Table:
    def __init__(self):
        self.players = []
        self.deck = Deck([])
        self.pot = Pot()

    def __repr__(self):
        """Implements the repr() function.

        >>> repr(Table())
        'Table([], Deck([]), Pot(0))'
         """
        return 'Table({}, {}, {})'.format(self.players, self.deck, self.pot)

    def __eq__(self, other):
        """Implement the equality function.

        >>> a = Table()
        >>> b = Table()
        >>> a == b
        True
        >>> a.players = [Player('Eric', 8000), Player('Stephen', 8001)]
        >>> a == b
        False
        """
        return (
            self.players == other.players and
            self.deck == other.deck and
            self.pot == other.pot
        )

    def __str__(self):
        r"""Return a string that will print a picture of the table.

        >>> t = Table()
        >>> t.players = [Player('Eric', 8000), Player('Stephen', 8001)]
        >>> t.players[0].hand.hand_list = [Card('H', '8'), Card('C', 'J')]
        >>> t.players[1].hand.hand_list = [Card('S', 'A'), Card('D', 'J')]
        >>> str(t)  # doctest: +NORMALIZE_WHITESPACE
        'Name: Eric        Hand: 8-H J-C                 Stash: 100
        Status: play\n\n          Pot: 0\n\nName: Stephen     Hand: A-S J-D
        Stash: 100   Status: play\n\n'
        """
        out_string_list = []
        for player in self.players:
            out_str = 'Name: {:10s}  Hand: '.format(player.name)
            out_str += ' '.join(['{}-{}'.format(card.rank, card.suit)
                                 for card in player.hand.hand_list]).ljust(24)
            out_str += 'Stash: {}   Status: {}'.format(player.stash.value,
                                                       player.status)
            out_string_list += [out_str]
        pot_string = ' '*10 + 'Pot: {}'.format(self.pot.value)
        return '\n\n'.join([out_string_list[0], pot_string,
                            out_string_list[1], ''])



