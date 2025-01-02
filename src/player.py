from src.deck import Card


class Player:
    def __init__(self, card_one, card_two):
        if type(card_one) is not Card or type(card_two) is not Card:
            raise TypeError("A player hand can only consist of Card objects")

        self.hand = [card_one, card_two]
