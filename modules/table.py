"""The Table class, which contains the players, pot, burn pile and hand number.

Initializes to no players, a pot with 0 value, an empty burn pile and 0 hand #.
str() function renders the table.  This is for server info only.
find_first_player() returns the index (in players[]) who should be dealt first.
"""

from player import Player
from pot import Pot
from card import Card
from burn import Burn
from server import PORTS


class Table:
    def __init__(self):
        self.players = []
        self.pot = Pot()
        self.burn = Burn()
        self.hand_num = 0

    def __repr__(self):
        """Implements the repr() function.

        >>> repr(Table())
        'Table([], Pot(0), Burn([]), 0)'
        """
        return 'Table({}, {}, {}, {})'.format(self.players, self.pot,
                                              self.burn, self.hand_num)

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
            self.pot == other.pot and
            self.burn == other.burn and
            self.hand_num == other.hand_num
        )

    def __str__(self):
        r"""Return a string that will print a picture of the table.

        >>> t = Table()
        >>> t.players = [Player('Eric', 8000), Player('Stephen', 8001)]
        >>> t.players[0].hand.hand_list = [Card('H', '8'), Card('C', 'J')]
        >>> t.players[1].hand.hand_list = [Card('S', 'A'), Card('D', 'J')]
        >>> str(t)  # doctest: +NORMALIZE_WHITESPACE
        'Name: Eric        Hand: 8-H J-C                 Stash: 100
        Status: play\n\n          Pot: 0   Hand #: 0\n\nName: Stephen
        Hand: A-S J-D                 Stash: 100   Status: play'
        """
        out_string_list = []
        for player in self.players:
            out_string = 'Name: {:10s}  Hand: '.format(player.name)
            out_string += ''.join(['{}-{} '.format(c.rank, c.suit)
                                   for c in player.hand.hand_list]).ljust(24)
            out_string += 'Stash: {}  Status: {}'.format(player.stash.value,
                                                         player.status)
            out_string_list += [out_string]
        pot_string = ' '*10 + 'Pot: {}   Hand #: {}'.format(self.pot.value,
                                                          self.hand_num)
        return '\n\n'.join([out_string_list[0], pot_string, out_string_list[1]])


def find_first_player(hand_num):
    """Return the index of the player to be dealt first.

    It presumes that the number of players is equal to the number of PORTS.

    >>> find_first_player(0)
    0
    >>> find_first_player(3)
    1
    """
    return hand_num % len(PORTS)
