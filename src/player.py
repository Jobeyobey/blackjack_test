from src.deck import Card


class Player:
    def __init__(self, card_one, card_two):
        if type(card_one) is not Card or type(card_two) is not Card:
            raise TypeError("A player hand can only consist of Card objects")

        self.hand = [card_one, card_two]

    def get_score(self):
        score = 0
        ace_count = 0

        for card in self.hand:
            score += card.value_card(card)
            if card.rank == "Ace":
                ace_count += 1

        # If score is over 21 and there are remaining ace cards valued at 11, convert to 1 (one by one)
        while score > 21:
            if ace_count > 0:
                score -= 10
            else:
                break

        return score
