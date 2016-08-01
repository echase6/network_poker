"""Chip management functions.


place_bet() manages chip motion when placing a bet.
  Modifies player and pot in-place.
  Returns True if the bet could be placed (based on amount), False otherwise.

calc_chips()
  Returns a chip dict with the quantity of chips for a given value.

collect_winnings()
  Move the winnings to the player.
  Modifies player and pot in-place.

"""

from player import Player
from pot import Pot

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 75, 0)
GOLD = (0, 75, 75)
RED = (175, 0, 0)
DENOMINATIONS = ['25', '5', '1']
DENOM_COLORS = [GREEN, RED, WHITE]


def place_bet(amount, player, pot):
    """Manage chip motion when placing a bet.

    Modifies player and pot in-place.
    Return True if the bet can be placed based on amount, False otherwise.
    >>> a = Player('Eric')
    >>> pot = Pot()
    >>> pot.value = 10
    >>> place_bet(10, a, pot)
    True
    >>> a.stash.value
    90
    >>> pot.value
    20
    >>> place_bet(100, a, pot)
    False
    """
    player_amt = player.stash.value
    if amount > player_amt:
        return False
    player.stash.value = player_amt - amount
    pot.value += amount
    return True


# def calc_value(chip_dict):
#     """Calculate the value of the player's stash.
#
#     >>> a = Player('Eric')
#     >>> calc_value(a.stash.chips)
#     100
#     """
#     return sum([qty * int(denom) for denom, qty in chip_dict.items()])
#

def calc_chips(amount):
    """Returns a chip dict with the quantity of chips for a given value.

    Entries exist even if no chip present.

    >>> sorted(calc_chips(37).items())
    [('1', 2), ('10', 1), ('25', 1), ('5', 0), ('50', 0)]
    """
    chip_dict = {}
    for denom in DENOMINATIONS:
        num = amount // int(denom)
        amount -= num * int(denom)
        chip_dict[denom] = num
    return chip_dict


def collect_winnings(player, pot):
    """Move the winnings to the player.

    Modifies player and pot in-place

    >>> a = Player('Eric')
    >>> pot = Pot()
    >>> pot.value = 20
    >>> collect_winnings(a, pot)
    >>> a.stash.value
    120
    >>> pot.value
    0
    """
    player.stash.value += pot.value
    pot.value = 0
