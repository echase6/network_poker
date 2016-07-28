"""The Pot class, which is the quantity of chips that have been better.

The pot is a dictionary of chip: quantity pairs.
The pot will have all chip denominations populated, even if quantity is zero.
"""


class Pot:
    def __init__(self):
        self.chips = ({
             '50': 0,
             '25': 0,
             '10': 0,
             '5': 0,
             '1': 0
        })

    def __repr__(self):
        """Implements the repr() function.

        >>> sorted(Pot().chips.items())
        [('1', 0), ('10', 0), ('25', 0), ('5', 0), ('50', 0)]
         """
        return 'Pot({})'.format(self.chips)

    def __eq__(self, other):
        """Implement the equality function.

        >>> Pot() == Pot()
        True
        >>> a = Pot()
        >>> b = Pot()
        >>> a.chips['25'] = 2
        >>> a == b
        False
        """
        return self.chips == other.chips
