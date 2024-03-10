from unittest import TestCase

from lib.board import BoardNode
from lib.cubecoordinate import CubeCoordinate
from lib.tile import Tile, TileType

class CreationTestCase(TestCase):
    
    def test_creation_normal(self):
        bn = BoardNode(CubeCoordinate(0,0,0))
        bn = BoardNode(CubeCoordinate(0,0,0),
                Tile(TileType.PLAINS, TileType.from_string("PPPPPP")))
                
                
class InterfaceTestCase(TestCase):
    
    def setUp(self):
        self.noTile = BoardNode(CubeCoordinate(0,0,0))
        self.yesTile = BoardNode(CubeCoordinate(0,0,0),
                Tile(TileType.PLAINS, TileType.from_string("PPPPPP")))
                
                
    def test_has_tile(self):
        self.assertTrue(self.yesTile.has_tile())
        self.assertFalse(self.noTile.has_tile())