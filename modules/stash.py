"""The Stash class, which is the quantity of chips for one player.

The stash is a dictionary of chip: quantity pairs.
The stash will have all chip denominations populated, even if quantity is zero.
Initial stash for a player is two '50' chips.
"""


class Stash:
    def __init__(self):
        self.value = 100

    def __repr__(self):
        """Implements the repr() function.

        >>> repr(Stash())
        'Stash(100)'
         """
        return 'Stash({})'.format(self.value)

    def __eq__(self, other):
        """Implement the equality function.

        >>> Stash() == Stash()
        True
        >>> a = Stash()
        >>> b = Stash()
        >>> a.value = 2
        >>> a == b
        False
        """
        return self.value == other.value
