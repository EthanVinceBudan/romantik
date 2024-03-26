from unittest import TestCase

from lib.deck import Deck
from lib.tile import Tile


class DeckTestCase(TestCase):

    def test_draw(self):
        deck = Deck(10)
        for i in range(10):
            tile = deck.draw()
            self.assertIsInstance(tile, Tile)
        self.assertIsNone(deck.draw())
