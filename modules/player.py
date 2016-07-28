"""The Player class, which contains the hand, stash and status of one player.

Initially, hand has no cards, stash has value of 100, and status is 'play'
"""

from hand import Hand
from stash import Stash


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.stash = Stash()
        self.status = 'play'

    def __repr__(self):
        """Implements the repr() function.

        >>> repr(Player('Eric'))
        'Player(Eric, Hand([]), Stash(100), play)'
         """
        return 'Player({}, {}, {}, {})'.format(self.name, self.hand,
                                               self.stash, self.status)

    def __eq__(self, other):
        """Implement the equality function.

        >>> Player('Eric') == Player('Eric')
        True
        >>> Player('Stephen') == Player('Eric')
        False
        """
        return (
            self.name == other.name and
            self.hand == other.hand and
            self.stash == other.stash and
            self.status == other.status
        )
