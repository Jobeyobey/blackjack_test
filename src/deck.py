from enum import Enum


class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    @staticmethod
    def create_deck():
        cards = []

        for suit in Suits:
            for rank in Ranks:
                cards.append(Card(suit, rank))

        return cards


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Suits(Enum):
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLUBS = 4


Ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
