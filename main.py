from card import Card
from hand import Hand
from stash import Stash
from pot import Pot
from player import Player
from table import Table
from deck import Deck



def main():
    t = Table()
    a = Player('Eric')
    b = Player('Stephen')
    t.players = [a, b]
    print(str(t))


if __name__ == '__main__':
    main()