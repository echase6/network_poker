"""A module for the network poker app that contains various functions for the betting loop of the game"""

from player import Player
from table import Table
from server import message_to_client, answer_from_client



def bet_loop(table, clients):
    """The meta bet loop"""
    output = True # only changes if someone folds
    player_1 = table.players[0]
    msg_player_1 = clients[0]
    player_2 = table.players[1]
    msg_player_2 = clients[1]
    while player_1.status != 'play' and table.pot != 0:
        message_to_client('Would you like to Fold, Raise, or Check?', player_1)
        response = answer_from_client(player_1)
        if response == 'Fold':
            output = _fold() # give money to other player, ending loop
        elif response == 'Check':
            player_1.status = 'play' # breaks out of loop, goes to player 2
        elif response == 'Raise':
            amount = _ante_raise(msg_player_1, msg_player_1) # raises
            call_or_fold(player_2, msg_player_2, amount, table.pot) # asks player_2 to call or fold, exits loop
        elif response == 'Call':
            _ante_call() # calls a raise, shouldn't be used first cycle

def _ante_raise(player, msg_player):
    """asks the client how much to raise, raises the pot, returns bet amount to ask the other player"""
    message_to_client('How much would you like to raise by?', msg_player)
    amount = answer_from_client(msg_player)
    place_bet(amount, player, table.pot)
    return amount


def _call_or_fold(player, msg_player, amount, pot):
    """Asks a player to call or fold"""
    message_to_client('The pot has been raised by {}, would you like to Call or Fold?'.format(amount), msg_player)
    response = answer_from_client(msg_player)
    if response == 'Fold':
       output =  _fold(player)
    elif response == 'Call':
        if place_bet(amount, player, pot):
            player.status = 'play'
        else:
            pot += player.stash
            player.stash -= player.stash
            player.status = 'play'
    return output

def _fold(folding_player, winning_player, pot):
    """Assigns the pot to the other player, returns false"""
    collect_winnings(winning_player, pot)