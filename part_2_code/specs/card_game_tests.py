import unittest
from src.card import Card
from src.card_game import *

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Hearts", 3)
        self.cards = [1, 2, 3, 4]
    

    def test_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self.card1))

    def test_can_return_highest_card_value(self):
        self.assertEqual(3, CardGame.highest_card(self.card1.value, self.card2.value))

    def test_can_return_total_card_value(self):
        self.assertEqual('You have a total of 10', CardGame.cards_total(self.cards))


