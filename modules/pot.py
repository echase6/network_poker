"""The Pot class, which is the quantity of chips that have been better.

The pot is a dictionary of chip: quantity pairs.
The pot will have all chip denominations populated, even if quantity is zero.
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
