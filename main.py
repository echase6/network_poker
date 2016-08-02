"""Network Poker project.

This is a collaborative project between Stephen Muller and Eric Chase.

Usage:
  -- Run main.py on the machine that is to be the server.
     It will reply with its address.  This can be changed from localhost
       to an external IP in the start_server() module in server.py
  -- Run client.py on a machine that is to be one of the clients (players).
     It will ask for a host address; this is the one the server gave (above).
     First client should choose port 8000.
  -- Run client.py on a second machine for the 2nd player.
     Enter the host address and port 8001.
  Note:  Both clients will see a GUI and I/O message/response is through
     the command-line.

Modules:
  connect_to_clients() -- establishes connections to clients and gets names.
  buy_in() -- moves buy-in amount from players to pot to begin round.
  deal_round() -- deal cards to the players
  send_table_to_clients() -- sent table info to both clients for rendering
  bet_loop_dummy() -- test betting loop to exercise functions w/o actual betting
  close_out_hand() -- find winner, distribute winnings, and inform players
  test_for_next_round() -- find out if another round is to be played
"""


import jsonpickle
from card import Card, SUITS, RANKS
from hand import Hand, generate_hand, compare_hands
from stash import Stash
from pot import Pot
from player import Player
from table import Table
from chip import place_bet, collect_winnings
from bet import bet_loop
from deck import Deck, generate_deck, shuffle_the_deck, draw_card_from_deck
from server import start_server, connect_client, message_to_client
from server import answer_from_client, send_table_to_client, PORTS


def connect_to_clients(t):
    """Establish the connections to the clients.

    Modifies table (t) with Player info in-place
    Returns clients (a list of two)
    """
    sockets = start_server()
    clients = [connect_client(s) for s in sockets]
    for i, client in enumerate(clients):
        message_to_client('What is your name?', client)
        name = answer_from_client(client)
        print('{} joined'.format(name))
        t.players += [Player(name, PORTS[i])]
    return clients


def buy_in(t, amt):
    """Buy the players in.

    Buy-in set to amt (dollars).
    """
    for player in t.players:
        place_bet(amt, player, t.pot)


def deal_round(t, deck):
    """Deal a hand to each of the players.  Two cards if the first round."""
    if len(t.players[0].hand.hand_list) <= 1:
        index = 2
    else:
        index = 1
    for i in range(index):
        for player in t.players:
            player.hand.hand_list += [draw_card_from_deck(deck)]


def send_table_to_clients(t, clients):
    """Send table to clients for their review."""
    for client in clients:
        send_table_to_client(t, client)


def bet_loop_dummy(t, clients):
    """This is a dummy loop to enable testing while the real loop gets written."""
    for i, client in enumerate(clients):
        message_to_client('Press any key?', client)
        _ = answer_from_client(client)
        place_bet(1, t.players[i], t.pot)
    return True


def close_out_hand(t, clients):
    """Close out the hand, find the winner, distribute the winnings."""

    winner = compare_hands(t.players[0].hand, t.players[1].hand)
    if winner == 'P1':
        collect_winnings(t.players[0], t.pot)
        winner_name = t.players[0].name
    else:
        collect_winnings(t.players[1], t.pot)
        winner_name = t.players[1].name
    send_table_to_clients(t, clients)
    for index, client in enumerate(clients):
        message_to_client('{} wins!\n'.format(winner_name), client)


def test_for_next_hand(t, clients):
    """See if there should be another hand."""
    if any([player.stash.value == 0 for player in t.players]):
        return False
    for client in clients:
        message_to_client('Want to keep playing?', client)
        answer = answer_from_client(client)
        if answer[0].lower() == 'n':
            return False
    return True


def main():
    t = Table()
    t.players = []
    clients = connect_to_clients(t)
    keep_playing = True
    print(str(t))
    while keep_playing:
        deck = generate_deck(SUITS, RANKS)
        shuffle_the_deck(deck)
        buy_in(t, 10)
        for player in t.players:
            player.hand.hand_list = []
        for i in range(4):
            deal_round(t, deck)
            send_table_to_clients(t, clients)
            if not bet_loop(t, clients):
                break
        close_out_hand(t, clients)
        keep_playing = test_for_next_hand(t, clients)


if __name__ == '__main__':
    main()