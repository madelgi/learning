import random


class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def _convert_num(self):
        if self.rank == 11:
            return "Jack"
        elif self.rank == 12:
            return "Queen"
        elif self.rank == 13:
            return "King"
        elif self.rank == 1:
            return "Ace"
        else:
            return str(self.rank)

    def __str__(self):
        return self._convert_num() + " of " + self.suit


class Deck(object):

    def __init__(self):
        self.deck = []

    def build_deck(self):
        suits = ['clubs', 'spades', 'hearts', 'diamonds']

        for suit in suits:
            for rank in xrange(1, 14):
                self.deck.append(Card(suit, rank))

    def __str__(self):
        string = ''
        for i in self.deck:
            string += str(i) + '\n'

        return string

    def shuffle(self):
        random.shuffle(self.deck)


def main():
    a = Deck()
    a.build_deck()
    print a
    a.shuffle()
    print a
