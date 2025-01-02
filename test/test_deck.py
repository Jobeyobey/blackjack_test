import unittest
from src.deck import Deck
from src.deck import Suits


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_number_of_cards(self):
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_number_of_suits(self):
        unique_suits = []

        for card in self.deck.cards:
            if card.suit not in unique_suits:
                unique_suits.append(card.suit)

        number_of_suits = len(unique_suits)
        self.assertEqual(number_of_suits, 4)

    def test_number_of_ranks(self):
        unique_ranks = []

        for card in self.deck.cards:
            if card.rank not in unique_ranks:
                unique_ranks.append(card.rank)

        number_of_ranks = len(unique_ranks)
        self.assertEqual(number_of_ranks, 13)

    def test_cards_correct_rank_and_suit(self):
        unique_cards = [
            (Suits.HEARTS, "Ace"),
            (Suits.HEARTS, "2"),
            (Suits.HEARTS, "3"),
            (Suits.HEARTS, "4"),
            (Suits.HEARTS, "5"),
            (Suits.HEARTS, "6"),
            (Suits.HEARTS, "7"),
            (Suits.HEARTS, "8"),
            (Suits.HEARTS, "9"),
            (Suits.HEARTS, "10"),
            (Suits.HEARTS, "Jack"),
            (Suits.HEARTS, "Queen"),
            (Suits.HEARTS, "King"),
            (Suits.DIAMONDS, "Ace"),
            (Suits.DIAMONDS, "2"),
            (Suits.DIAMONDS, "3"),
            (Suits.DIAMONDS, "4"),
            (Suits.DIAMONDS, "5"),
            (Suits.DIAMONDS, "6"),
            (Suits.DIAMONDS, "7"),
            (Suits.DIAMONDS, "8"),
            (Suits.DIAMONDS, "9"),
            (Suits.DIAMONDS, "10"),
            (Suits.DIAMONDS, "Jack"),
            (Suits.DIAMONDS, "Queen"),
            (Suits.DIAMONDS, "King"),
            (Suits.SPADES, "Ace"),
            (Suits.SPADES, "2"),
            (Suits.SPADES, "3"),
            (Suits.SPADES, "4"),
            (Suits.SPADES, "5"),
            (Suits.SPADES, "6"),
            (Suits.SPADES, "7"),
            (Suits.SPADES, "8"),
            (Suits.SPADES, "9"),
            (Suits.SPADES, "10"),
            (Suits.SPADES, "Jack"),
            (Suits.SPADES, "Queen"),
            (Suits.SPADES, "King"),
            (Suits.CLUBS, "Ace"),
            (Suits.CLUBS, "2"),
            (Suits.CLUBS, "3"),
            (Suits.CLUBS, "4"),
            (Suits.CLUBS, "5"),
            (Suits.CLUBS, "6"),
            (Suits.CLUBS, "7"),
            (Suits.CLUBS, "8"),
            (Suits.CLUBS, "9"),
            (Suits.CLUBS, "10"),
            (Suits.CLUBS, "Jack"),
            (Suits.CLUBS, "Queen"),
            (Suits.CLUBS, "King"),
        ]
        counter = 0

        for card in self.deck.cards:
            for unique_card in unique_cards:
                if card.suit == unique_card[0] and card.rank == unique_card[1]:
                    counter += 1
                    unique_cards.remove(unique_card)

        self.assertEqual(counter, 52)


if __name__ == "__main__":
    unittest.main()
