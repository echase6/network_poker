from card import Card, SUITS, RANKS
from hand import Hand, generate_hand
from stash import Stash
from pot import Pot
from player import Player
from table import Table
from deck import Deck, generate_deck, shuffle_the_deck


def main():
    deck = generate_deck(SUITS, RANKS)
    shuffle_the_deck(deck)
    t = Table()
    a = Player('Eric')
    a.hand = generate_hand(deck)
    b = Player('Stephen')
    b.hand = generate_hand(deck)
    t.players = [a, b]
    print(str(t))


if __name__ == '__main__':
    main()