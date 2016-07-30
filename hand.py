"""a class for storing poker hands"""

from deck import Deck
from deck import draw_card_from_deck
from card import Card

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Hand:
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
    """adds a card to a hand
    >>> generate_hand(Deck([Card('H', '7'), Card('H', '8')]))
    Hand([Card('H', '8'), Card('H', '7')])
    """
    return Hand([draw_card_from_deck(deck), draw_card_from_deck(deck)])


def compare_hands(hand_1, hand_2):
    """takes two hands and checks for a winner"""
    _assi


def _assign_hand_rank(hand):
    """Assigns a hand a rank for future comparison"""
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
    """checks for the presence

    >>> _check_for_2_pair(Hand([Card('H', '10'), Card('C', '10'), Card('S', 'A'), Card('D', '9'), Card('H', 'A')]))
    True
    >>> _check_for_2_pair(Hand([Card('H', '2'), Card('C', '3'), Card('S', '4'), Card('D', '10'), Card('H', 'A')]))
    False
    """
    output = False
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    card_counts = []
    for item in grouping:
        card_counts.append(grouping[item])
    card_counts = sorted(card_counts)
    if card_counts[2] == 2 and card_counts[1] == 2:
        output = True
    return output


def _check_for_4_of_a_kind(hand):
    """checks to see if the hand has four like cards

    >>> _check_for_4_of_a_kind(Hand([Card('H', '10'), Card('C', '10'), Card('S', '10'), Card('D', '10'), Card('H', 'A')]))
    True
    >>> _check_for_4_of_a_kind(Hand([Card('H', '9'), Card('C', '10'), Card('S', '10'), Card('D', '10'), Card('H', 'A')]))
    False
    """
    output = False
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    for item in grouping:
        if grouping[item] == 4:
            output = True
    return output


def _check_for_full_house(hand):
    """checks to see if there is a full house in the hand

    >>> _check_for_full_house(Hand([Card('H', '10'), Card('C', '10'), Card('S', 'A'), Card('D', '10'), Card('H', 'A')]))
    True
    >>> _check_for_full_house(Hand([Card('H', '9'), Card('C', '10'), Card('S', '10'), Card('D', '10'), Card('H', 'A')]))
    False
    """
    output = False
    pair_truth = False
    trips_truth = False
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    for item in grouping:
        if grouping[item] == 3:
            trips_truth = True
        elif grouping[item] == 2:
            pair_truth = True
    if pair_truth is True and trips_truth is True:
        output = True
    return output


def _check_for_three(hand):
    """checks to see if a players hand has three of a kind

    >>> _check_for_three(Hand([Card('H', '10'), Card('C', '10'), Card('S', 'A'), Card('D', '10'), Card('H', 'A')]))
    True
    >>> _check_for_three(Hand([Card('H', '9'), Card('C', '5'), Card('S', '10'), Card('D', '10'), Card('H', 'A')]))
    False
    """
    output = False
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    for item in grouping:
        if grouping[item] == 3:
            output = True
    return output


def _check_for_two(hand):
    """checks to see if a players hand has three of a kind

    >>> _check_for_two(Hand([Card('H', '10'), Card('C', '9'), Card('S', '3'), Card('D', '10'), Card('H', 'A')]))
    True
    >>> _check_for_three(Hand([Card('H', '9'), Card('C', '5'), Card('S', '10'), Card('D', '7'), Card('H', 'A')]))
    False
    """
    output = False
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    for item in grouping:
        if grouping[item] == 2:
            output = True
    return output


def _check_for_straight_flush(hand):
    """Returns true if a hand has a straight flush in it

    >>> _check_for_straight_flush(Hand([Card('H', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    True
    >>> _check_for_straight_flush(Hand([Card('C', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    False
    """
    flush = _check_for_flush(hand)
    straight = _check_for_straight(hand)
    if flush == True and straight == True:
        output = True
    else:
        output = False
    return output


def _check_for_flush(hand):
    """checks a hand for a flush

    >>> _check_for_flush(Hand([Card('H', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    True

    >>> _check_for_flush(Hand([Card('C', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    False
    """
    suit_checker = hand.hand_list[0].suit
    truth_check = all(card.suit == suit_checker for card in hand.hand_list)
    # truth_check = ''
    # for card in hand.hand_list:
    #     if card.suit == suit_checker:
    #         truth_check = True
    #     else:
    #         truth_check = False
    return truth_check


def _check_for_straight(hand):
    """runs a test against a hand to see if there is a straight

    >>> _check_for_straight(Hand([Card('C', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    True
    >>> _check_for_straight(Hand([Card('C', '2'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6')]))
    True
    >>> _check_for_straight(Hand([Card('C', '8'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6')]))
    False
    >>> _check_for_straight(Hand([Card('C', '7'), Card('H', '3'), Card('H', '4'), Card('H', '5'), Card('H', '6')]))
    True
    """
    card_val_list = []
    for card in hand.hand_list:
        card_val_list.append(RANKS.index(card.rank))
    card_val_list.sort()
    temp_range = list(range(card_val_list[0], card_val_list[4]+1))
    temp_sort = sorted(card_val_list)
    if temp_sort == temp_range:
        output = True
    else:
        output = False
    return output


def _check_for_royal_flush(hand):
    """tests for a royal flush

    >>> _check_for_royal_flush(Hand([Card('H', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    True

    >>> _check_for_royal_flush(Hand([Card('H', '8'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    False
    """
    flush = _check_for_flush(hand)
    straight = _check_for_straight(hand)
    royal = _check_royalty(hand)
    if(
        flush == True and
        straight == True and
        royal == True
    ):
        output = True
    else:
        output = False
    return output


def _check_royalty(hand):
    """checks if a hand contains only royal cards

    >>> _check_royalty(Hand([Card('H', '10'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    True

    >>> _check_royalty(Hand([Card('H', '8'), Card('H', 'J'), Card('H', 'Q'), Card('H', 'K'), Card('H', 'A')]))
    False
    """
    ace_truthiness = False
    ten_truthiness = False
    for card in hand.hand_list:
        if 'A' in card.rank:
            ace_truthiness = True
    for card in hand.hand_list:
        if '10' in card.rank:
            ten_truthiness = True
    if ace_truthiness == True and ten_truthiness == True:
        output = True
    else:
        output = False
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


def _group_by_length(grouping):
    """simplifies the group by output when checking for pairs/triplets/quads"""


def rank_key(card):
    """generates a key for the group by function

    >>> rank_key(Card('C', '10'))
    '10'
    """
    return card.rank
