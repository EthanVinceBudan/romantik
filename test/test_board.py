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
        
        
class InterfaceTestCase(TestCase):

    def setUp(self):
        self.b = Board()
        

    def test_expand_board(self):
        p1 = CubeCoordinate(1, 0, -1)
        p2 = CubeCoordinate(0, 1, -1)
        self.assertTrue(p1 in self.b._nodemap)
        self.assertTrue(p2 in self.b._nodemap)
        self.assertTrue(p1 in self.b._border_coords)
        self.assertTrue(p2 in self.b._border_coords)

        new_count1 = self.b.expand(p1)
        new_count2 = self.b.expand(p2)
        self.assertEqual(new_count1, 3)
        self.assertEqual(new_count2, 2)
        self.assertEqual(self.b.size, 12)
        self.assertEqual(len(self.b.border_nodes()), 9)
        self.assertFalse(p1 in self.b._border_coords)
        self.assertFalse(p2 in self.b._border_coords)
        self.assertTrue(CubeCoordinate(2, 0, -2) in self.b._border_coords)
        self.assertTrue(CubeCoordinate(2, -1, -1) in self.b._border_coords)
        self.assertTrue(CubeCoordinate(1, 1, -2) in self.b._border_coords)
        
        
    def test_expand_board_hole(self):
        coordsToExpand = [
            CubeCoordinate(0,-1,1),
            CubeCoordinate(0,-2,2),
            CubeCoordinate(1,-3,2),
            CubeCoordinate(2,-4,2),
            CubeCoordinate(3,-4,1),
            CubeCoordinate(4,-4,0),
            CubeCoordinate(4,-3,-1),
            CubeCoordinate(4,-2,-2),
            CubeCoordinate(3,-1,-2),
            CubeCoordinate(2,0,-2),
            CubeCoordinate(1,0,-1)
        ]
        
        newCounts = []
        for coord in coordsToExpand:
            newCounts.append(self.b.expand(coord))
            
        self.assertEqual(newCounts, [3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0])
        self.assertNotIn(CubeCoordinate(2,-2,0), self.b._nodemap)
        
        # fill in hole
        newCount = self.b.expand(CubeCoordinate(1,-1,0))
        
        self.assertEqual(newCount, 1)
        self.assertIn(CubeCoordinate(2,-2,0), self.b._nodemap)
        self.assertFalse(self.b._nodemap[CubeCoordinate(2,-2,0)].is_border())
        self.assertNotIn(CubeCoordinate(2,-2,0), self.b._border_coords)
