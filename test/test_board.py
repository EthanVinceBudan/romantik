from unittest import TestCase

from lib.board import Board
from lib.cubecoordinate import CubeCoordinate

class CreationTestCase(TestCase):

    def test_creation_normal(self):
        b = Board()
        self.assertEqual(b.size, 7)
        self.assertEqual(len(b.border_nodes()), 6)
        self.assertTrue(all(i in b._nodemap for i in b._border_coords))
        self.assertTrue(
            not any(b._nodemap[i].has_tile() for i in b._border_coords))
        self.assertTrue(sum(i.has_tile() for i in b._nodemap.values()), 1)

    def test_expand_board(self):
        b = Board()

        p1 = CubeCoordinate(1, 0, -1)
        p2 = CubeCoordinate(0, 1, -1)
        self.assertTrue(p1 in b._nodemap)
        self.assertTrue(p2 in b._nodemap)
        self.assertTrue(p1 in b._border_coords)
        self.assertTrue(p2 in b._border_coords)

        new_count1 = b.expand(p1)
        new_count2 = b.expand(p2)
        self.assertEqual(new_count1, 3)
        self.assertEqual(new_count2, 2)
        self.assertEqual(b.size, 12)
        self.assertEqual(len(b.border_nodes()), 9)
        self.assertFalse(p1 in b._border_coords)
        self.assertFalse(p2 in b._border_coords)
        self.assertTrue(CubeCoordinate(2, 0, -2) in b._border_coords)
        self.assertTrue(CubeCoordinate(2, -1, -1) in b._border_coords)
        self.assertTrue(CubeCoordinate(1, 1, -2) in b._border_coords)
