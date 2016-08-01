"""The Pot class, which is the value of chips in the pot.

The pot has a single variable 'value' representing dollars.
Initial pot is 0.
"""


class Pot:
    def __init__(self):
        self.value = 0

    def __repr__(self):
        """Implements the repr() function.

        >>> repr(Pot())
        'Pot(0)'
        """
        return 'Pot({})'.format(self.value)

    def __eq__(self, other):
        """Implement the equality function.

        >>> Pot() == Pot()
        True
        >>> a = Pot()
        >>> b = Pot()
        >>> a.value = 25
        >>> a == b
        False
        """
        return self.value == other.value
