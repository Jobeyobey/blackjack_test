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

    @staticmethod
    def value_card(card):
        match card.rank:
            case "2":
                return 2
            case "3":
                return 3
            case "4":
                return 4
            case "5":
                return 5
            case "6":
                return 6
            case "7":
                return 7
            case "8":
                return 8
            case "9":
                return 9
            case "10" | "Jack" | "Queen" | "King":
                return 10
            case "Ace":
                return 11
            case _:
                raise Exception("Value not valid")


class Suits(Enum):
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLUBS = 4


Ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
