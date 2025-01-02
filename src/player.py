from src.deck import Card


class Player:
    def __init__(self, card_one, card_two):
        if type(card_one) is not Card or type(card_two) is not Card:
            raise TypeError("A player hand can only consist of Card objects")

        self.hand = [card_one, card_two]

    def hit(self, deck):
        self.hand.append(deck.cards.pop(0))
        print(self.get_score())

    def stand(self):
        # In full game, this would remove the player from active players
        return self.get_score()

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

    def check_valid_hand(self):
        if self.get_score() > 21:
            return False
        return True

    def go_bust(self):
        # In full game, this would remove the player from the round after invalid hand found
        pass
