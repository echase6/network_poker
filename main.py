import jsonpickle
from card import Card, SUITS, RANKS
from hand import Hand, generate_hand, compare_hands
from stash import Stash
from pot import Pot
from player import Player
from table import Table
from deck import Deck, generate_deck, shuffle_the_deck
from server import start_server, connect_client, message_to_client
from server import answer_from_client, send_table_to_client, PORTS


def main():
    deck = generate_deck(SUITS, RANKS)
    shuffle_the_deck(deck)
    t = Table()
    t.players = []
    sockets = start_server()
    clients = [connect_client(s) for s in sockets]
    for i, client in enumerate(clients):
        message_to_client('What is your name?', client)
        name = answer_from_client(client)
        print('{} joined'.format(name))
        player = Player(name, PORTS[i])
        player.hand = generate_hand(deck)
        player.hand.append(draw_card_from_deck(deck))
        player.hand.append(draw_card_from_deck(deck))
        player.hand.append(draw_card_from_deck(deck))
        t.players += [player]
    print(str(t))
    for client in clients:
        send_table_to_client(t, client)
    #
    for player in t.players:
        buy_in()
    winner = compare_hands(t.players[0], t.players[1])




if __name__ == '__main__':
    main()