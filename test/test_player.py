import unittest
from src.player import Player
from src.deck import Card
from src.deck import Suits


class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.player = Player(Card(Suits.HEARTS, "5"), Card(Suits.SPADES, "Ace"))

    def tearDown(self):
        pass

    def test_number_of_cards(self):
        number_of_cards = len(self.player.hand)
        self.assertEqual(number_of_cards, 2)

    def test_player_hand_must_be_cards(self):
        with self.assertRaises(TypeError):
            new_player = Player(2, Card(Suits.DIAMONDS, "King"))
