from unittest import TestCase

from lib.board import Board
from lib.cubecoordinate import CubeCoordinate

class CreationTestCase(TestCase):

    def test_creation_normal(self):
        b = Board()
        self.assertEqual(b.size(), 7)
        self.assertEqual(len(b.edge_nodes()), 6)
        self.assertTrue(all(i in b.all_nodes() for i in b.edge_nodes()))
        self.assertTrue(not any(i.has_tile() for i in b.edge_nodes()))
        self.assertTrue(sum(i.has_tile() for i in b.all_nodes()), 1)
        