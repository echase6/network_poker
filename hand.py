"""a class for storing poker hands"""

from deck import Deck
from deck import draw_card_from_deck
from card import Card

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# ranks + index val for reference
# RANKS = (0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10), (9, J), (10, Q), (11, K), (12, A)

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

# def compare_hands(hand_1, hand_2):
#     """compares hands to check for a winner"""
#     ##win conditions royal flush > straight flush > flush > straight >
#     Royal flush.A, K, Q, J, 10, all
#     Straight flush
#     Four of akind
#     Full house
#     Flush
#     Straight
#     Three of a kind
#     pair

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
    grouping = group_by(hand.hand_list, rank_key)
    for item in grouping:
        grouping[item] = len(grouping[item])
    


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
    truth_check = ''
    for card in hand.hand_list:
        if card.suit == suit_checker:
            truth_check = True
        else:
            truth_check = False
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

def rank_key(card):
    """generates a key for the group by function

    >>> rank_key(Card('C', '10'))
    '10'
    """
    return card.rank
