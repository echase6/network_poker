"""The Player class, containing the name, hand, stash and status of one player.

When network ports are implemented this may contain the port ID as well.
Name get passed to it when first instantiated.
Initially, hand has no cards, stash has value of 100, and status is 'play'
"""

from hand import Hand
from stash import Stash
from table import Table


class Player:
    def __init__(self, name, port):
        self.name = name
        self.port = port
        self.hand = Hand([])
        self.stash = Stash()
        self.status = 'play'

    def __repr__(self):
        """Implements the repr() function.

        >>> repr(Player('Eric', 8000))
        'Player(Eric, 8000, Hand([]), Stash(100), play)'
         """
        return 'Player({}, {}, {}, {}, {})'.format(self.name, self.port,
                                                   self.hand, self.stash,
                                                   self.status)

    def __eq__(self, other):
        """Implement the equality function.

        >>> Player('Eric', 8000) == Player('Eric', 8000)
        True
        >>> Player('Stephen', 8001) == Player('Eric', 8000)
        False
        """
        return (
            self.name == other.name and
            self.port == other.port and
            self.hand == other.hand and
            self.stash == other.stash and
            self.status == other.status
        )

    def buy_in(self, player):
        """Charges the player 10 credits to join a round, or the remainder of their credits. Charges in place.

        10 credits to join into a round
        """
        if player.stash.value >= 10:
            player.stash.value -= 10
            table.pot += 10
        else:
            table.pot += player.stash
            player.stash.value -= player.stash.value



# def take_action(player, player_input):
#     """Takes player input and runs the appropriate function"""
#     if player_input == 'check':
#         break
#     elif player_input == 'raise':
#         _raise_pot()
#     elif player_input == 'call':
#         _call()
#     elif player_input == 'fold':
#         fold()
#
# def _raise_pot(player, player2):
#     """removes money from stash and places in pot if possible"""
#     amount = input('How much? ')
#     if stash >= amount:
#         player.stash =- amount
#         table.pot += amount
#         _call(player2, amount)
#     else:
#         print('You can\'t afford that')
#
# def _call(player, amount):
#     """Allows a player to call or fold, modifies values in place"""
#     response = input('The pot has been raised {}, would you like to call or fold? '.format(amount))
#     if response = 'call':
#         if player.stash >= amount:
#             player.stash -= amount
#             table.pot +=amount
#         else:
#             temp = player.stash
#             player.stash = 0
#             table.pot += temp
#     if response = 'fold':
#         break
#
# def _fold():
#     """Ends round, other player wins"""
#     assign_winner()




