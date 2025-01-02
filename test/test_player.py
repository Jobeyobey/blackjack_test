import unittest
from src.player import Player
from src.deck import Deck
from src.deck import Card
from src.deck import Suits


class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.player = Player(Card(Suits.HEARTS, "King"), Card(Suits.SPADES, "Ace"))
        self.deck = Deck()

    def tearDown(self):
        pass

    def test_number_of_cards(self):
        number_of_cards = len(self.player.hand)
        self.assertEqual(number_of_cards, 2)

    def test_player_hand_must_be_cards(self):
        with self.assertRaises(TypeError):
            new_player = Player(2, Card(Suits.DIAMONDS, "King"))

    def test_calculate_correct_score(self):
        player_two = Player(
            Card(
                Suits.DIAMONDS,
                "King",
            ),
            Card(Suits.CLUBS, "Queen"),
        )
        player_two.hand.append(Card(Suits.DIAMONDS, "Ace"))

        player_three = Player(
            Card(
                Suits.CLUBS,
                "9",
            ),
            Card(Suits.SPADES, "Ace"),
        )
        player_three.hand.append(Card(Suits.CLUBS, "Ace"))

        player_four = Player(Card(Suits.HEARTS, "5"), Card(Suits.HEARTS, "King"))
        player_four.hand.append(Card(Suits.CLUBS, "10"))

        score_one = self.player.get_score()
        score_two = player_two.get_score()
        score_three = player_three.get_score()
        score_four = player_four.get_score()

        self.assertEqual(score_one, 21)
        self.assertEqual(score_two, 21)
        self.assertEqual(score_three, 21)
        self.assertEqual(score_four, 25)

    def test_check_valid_hand(self):
        self.assertEqual(self.player.check_valid_hand(), True)

    def test_check_invalid_hand(self):
        invalid_player = Player(Card(Suits.HEARTS, "10"), Card(Suits.DIAMONDS, "10"))
        invalid_player.hand.append(Card(Suits.CLUBS, "2"))
        self.assertEqual(invalid_player.check_valid_hand(), False)

    def test_hit_adds_card_to_hand(self):
        self.player.hit(self.deck)
        hand_size = len(self.player.hand)

        self.assertEqual(hand_size, 3)

    def test_stand_returns_score(self):
        player_score = self.player.get_score()
        self.assertEqual(player_score, 21)
