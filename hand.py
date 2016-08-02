"""The Hand class for the Network Poker game.

Hands contain a list of Card class instances.

generate_hand() creates a new hand instance with two cards.
compare_hands() runs both hands through a series of functions that assign numerical values and returns p1 or p2 as the
winner of the round.
"""

from deck import Deck
from deck import draw_card_from_deck
from card import Card

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Hand:
    """Hand Class"""
    def __init__(self, hand_list):
        self.hand_list = hand_list

    def __eq__(self, other):
        """Return eq

        >>> (
        ... Hand([Card('H', '5'), Card('C', '2')]) ==
        ... Hand([Card('H', '5'), Card('C', '2')])
        ... )
        True
        >>> (
        ... Hand([Card('H', '5'), Card('C', '3')]) ==
        ... Hand([Card('H', '5'), Card('C', '2')])
        ... )
        False
        """
        return(
            self.hand_list == other.hand_list
        )

    def __repr__(self):
        """Return repr.

        >>> repr(Hand([Card('H', '5'), Card('C', '2')]))
        "Hand([Card('H', '5'), Card('C', '2')])"
        """
        return 'Hand({!r})'.format(
            self.hand_list
        )


def generate_hand(deck):
    """Creates a new instance of the hand class and assigns it two cards from the deck.

    >>> generate_hand(Deck([Card('H', '7'), Card('H', '8')]))
    Hand([Card('H', '8'), Card('H', '7')])
    """
    return Hand([draw_card_from_deck(deck), draw_card_from_deck(deck)])


def compare_hands(hand_1, hand_2):
    """Runs two hands through the assign rank function and compares their values. Returns 'P1' or 'p2'
    p2 wins by default if there is a tie.
    """
    hand_1_score = _assign_hand_rank(hand_1)
    hand_2_score = _assign_hand_rank(hand_2)
    if hand_1_score > hand_2_score:
        output = 'P1'
    else:
        output = 'p2'
    return output


def _assign_hand_rank(hand):
    """Assigns a hand a rank for comparison vs. the other player. Returns an integer.

    >>> _assign_hand_rank(Hand([Card('H', '9'), Card('C', '10'), Card('S', '10'), Card('D', '10'), Card('H', 'A')]))
    4
    >>> _assign_hand_rank(Hand([Card('H', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    10
    """
    if _check_for_royal_flush(hand):
        score = 10
    elif _check_for_straight_flush(hand):
        score = 9
    elif _check_for_4_of_a_kind(hand):
        score = 8
    elif _check_for_full_house(hand):
        score = 7
    elif _check_for_flush(hand):
        score = 6
    elif _check_for_straight(hand):
        score = 5
    elif _check_for_three(hand):
        score = 4
    elif _check_for_2_pair(hand):
        score = 3
    elif _check_for_two(hand):
        score = 2
    else:
        score = 1
    return score


def _check_for_2_pair(hand):
    """Checks for the presence of two pairs in a hand. Returns a boolean.

    >>> _check_for_2_pair(Hand([Card('H', '10'), Card('C', '10'), Card('S', 'A'), Card('D', '9'), Card('H', 'A')]))
    True
    >>> _check_for_2_pair(Hand([Card('H', '2'), Card('C', '3'), Card('S', '4'), Card('D', '10'), Card('H', 'A')]))
    False
    """
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    temp = [grouping[item] for item in grouping if grouping[item] == 2]
    return len(temp) == 2


def _check_for_4_of_a_kind(hand):
    """Groups the cards by rank and checks for any rank that has 4 items. Returns a boolean.

    >>> _check_for_4_of_a_kind(Hand([Card('H', '9'), Card('C', '9'), Card('S', '9'), Card('D', '9'), Card('H', 'A')]))
    True
    >>> _check_for_4_of_a_kind(Hand([Card('H', '9'), Card('C', 'A'), Card('S', '5'), Card('D', '4'), Card('H', 'A')]))
    False
    """
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    return any(grouping[item] == 4 for item in grouping)


def _check_for_full_house(hand):
    """Checks to see if a hand contains three of one card and two of another card. Returns a boolean.

    >>> _check_for_full_house(Hand([Card('H', '10'), Card('C', '10'), Card('S', 'A'), Card('D', '10'), Card('H', 'A')]))
    True
    >>> _check_for_full_house(Hand([Card('H', '9'), Card('C', '10'), Card('S', '10'), Card('D', '10'), Card('H', 'A')]))
    False
    """
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    return (
        any(grouping[item] == 3 for item in grouping) and
        any(grouping[item] == 2 for item in grouping)
    )


def _check_for_three(hand):
    """Checks for a three of a kind. Returns a boolean.

    Groups the cards by ranks, checks if any rank has three values in the list.

    >>> _check_for_three(Hand([Card('H', '10'), Card('C', '10'), Card('S', 'A'), Card('D', '10'), Card('H', 'A')]))
    True
    >>> _check_for_three(Hand([Card('H', '9'), Card('C', '5'), Card('S', '10'), Card('D', '10'), Card('H', 'A')]))
    False
    """
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    return any(grouping[item] == 3 for item in grouping)


def _check_for_two(hand):
    """Checks for a pair. Returns a boolean.

    Groups all of the rank values and checks for a rank with two associated values.

    >>> _check_for_two(Hand([Card('H', '10'), Card('C', '9'), Card('S', '3'), Card('D', '10'), Card('H', 'A')]))
    True
    >>> _check_for_three(Hand([Card('H', '9'), Card('C', '5'), Card('S', '10'), Card('D', '7'), Card('H', 'A')]))
    False
    """
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    return any(grouping[item] == 2 for item in grouping)


def _check_for_straight_flush(hand):
    """Runs a hand against the straight and flush functions to check if it's a straight flush. Returns a boolean.

    >>> _check_for_straight_flush(Hand(
    ... [Card('H', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    True
    >>> _check_for_straight_flush(Hand(
    ... [Card('C', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    False
    """
    flush = _check_for_flush(hand)
    straight = _check_for_straight(hand)
    return all([straight, flush])


def _check_for_flush(hand):
    """Checks for the presence of a flush. Returns a boolean.

    >>> _check_for_flush(Hand([Card('H', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    True

    >>> _check_for_flush(Hand([Card('C', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    False
    """
    suit_checker = hand.hand_list[0].suit
    return all(card.suit == suit_checker for card in hand.hand_list)


def _check_for_straight(hand):
    """Checks for the presence of a straight. Returns a boolean.

    Puts all of the ranks in a list, sorts the list, compares that list to a range based on the first and last element,
    if the list matches the range the function returns True.

    >>> _check_for_straight(Hand([Card('C', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    True
    >>> _check_for_straight(Hand([Card('C', '2'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6')]))
    True
    >>> _check_for_straight(Hand([Card('C', '8'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6')]))
    False
    >>> _check_for_straight(Hand([Card('C', '7'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6')]))
    True
    """
    card_val_list = [RANKS.index(card.rank) for card in hand.hand_list]
    card_val_list.sort()
    temp_range = list(range(card_val_list[0], card_val_list[4]+1))
    temp_sort = sorted(card_val_list)
    return temp_sort == temp_range


def _check_for_royal_flush(hand):
    """Checks for a flush, straight, and ace to see if the hand has a royal flush. Returns a boolean.

    >>> _check_for_royal_flush(Hand([Card('H', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    True

    >>> _check_for_royal_flush(Hand([Card('H', '8'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    False
    """
    flush = _check_for_flush(hand)
    straight = _check_for_straight(hand)
    royal = _check_royalty(hand)
    return all([flush, straight, royal])


def _check_royalty(hand):
    """Checks for the presence of an Ace in a hand. Returns a boolean.

    If a hand contains a straight and a flush the last thing to check is for an Ace to prove that it's a royal flush.

    >>> _check_royalty(Hand([Card('H', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    True

    >>> _check_royalty(Hand([Card('H', '8'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', '9')]))
    False
    """
    output = any(card.rank in 'A' for card in hand.hand_list)
    return output


def group_by(iterable, key):
    """Place each item in an iterable into a bucket based on calling the key
    function on the item."""
    group_to_items = {}
    for item in iterable:
        group = key(item)
        if group not in group_to_items:
            group_to_items[group] = []
        group_to_items[group].append(item)
    return group_to_items


def rank_key(card):
    """Generates a key for the group by function

    >>> rank_key(Card('C', '10'))
    '10'
    """
    return card.rank
