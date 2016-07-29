"""The Stash class, which is the value of chips for one player.

The stash has a single variable 'value' representing dollars.
Initial stash for a player is 100.
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
