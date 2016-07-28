"""Chip management functions."""

from stash import Stash
from player import Player
from pot import Pot


def place_bet(amount, player, pot):
    """Manage chip motion when placing a bet.

    Modifies player and pot in-place.
    Return True if the bet can be placed based on amount, False otherwise.
    >>> a = Player('Eric')
    >>> pot = Pot()
    >>> place_bet(10, a, pot)
    True
    >>> sorted(a.stash.chips)
    [['1', 0], ['10', 0], ['25', 1], ['5', 1], ['50', 1]]
    >>> sorted(pot.stash.chips)
    [['1', 0], ['10', 1], ['25', 0], ['5', 0], ['50', 0]]
    """
    player_amt = calc_value(player.stash)
    if amount > player_amt:
        return False
    player.stash.chips = calc_chips(player_amt - amount)
    return True


def calc_value(chip_dict):
    """Calculate the value of the player's stash.

    >>> a = Player('Eric')
    >>> calc_value(a.stash)
    100
    """
    return sum([qty * int(denom) for denom, qty in chip_dict.chips])


def calc_chips(amount):
    """Returns a chip dict with the quantity of chips for a given value.

    >>> sorted(calc_chips(37))
    [['1', 2], ['10', 1], ['25', 1], ['5', 0], ['50', 0]]
    """
    new_chip_dict = Stash()
    for qty, denom in new_chip_dict.chips:
        num = amount // int(denom)
        amount -= num * int(denom)
        new_chip_dict.chips[denom] = qty
    return new_chip_dict


def collect_winnings(player, pot):
    """Move the winnings to the player.

    Modifies player and pot in-place

    >>> a = Player('Eric')
    >>> pot = Pot()
    >>> pot.chips = {'50': 1, '25': 1, '10': 0, '5': 1, '1': 1}
    >>> collect_winnings(a, pot)
    >>> sorted(a.stash.chips)
    [['1', 1], ['10', 0], ['25', 1], ['5', 1], ['50', 3]]
    >>> sorted(pot.stash.chips)
    [['1', 0], ['10', 0], ['25', 0], ['5', 0], ['50', 0]]
    """
    amt_pot = calc_value(pot)
    amt_player = calc_value(player.stash)
    player.stash.chips = calc_chips(amt_pot + amt_player)
    pot.chips = calc_chips(0)


