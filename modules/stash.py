"""The Stash class, which is the quantity of chips for one player.

The stash is a dictionary of chip: quantity pairs.
The stash will have all chip denominations populated, even if quantity is zero.
Initial stash for a player is two '50' chips.
"""


class Stash:
    def __init__(self):
        self.chips = ({
             '50': 2,
             '25': 0,
             '10': 0,
             '5': 0,
             '1': 0
        })

    def __repr__(self):
        """Implements the repr() function.

        >>> sorted(Stash().chips.items())
        [('1', 0), ('10', 0), ('25', 0), ('5', 0), ('50', 2)]
         """
        return 'Stash({})'.format(self.chips)

    def __eq__(self, other):
        """Implement the equality function.

        >>> Stash() == Stash()
        True
        >>> a = Stash()
        >>> b = Stash()
        >>> a.chips['25'] = 2
        >>> a == b
        False
        """
        return self.chips == other.chips
