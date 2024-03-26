from unittest import TestCase

from lib.tile import Tile, TileType

class TileTypeTestCase(TestCase):
    
    def test_from_string(self):
        self.assertEqual(TileType.from_string("PPPPPP"), [TileType.PLAINS] * 6)
        self.assertEqual(TileType.from_string("PWHFLRT"), list(TileType))
        

class CreationTestCase(TestCase):
    
    def test_creation_normal(self):
        t = Tile(TileType.PLAINS, [TileType.PLAINS] * 6)
        t = Tile(TileType.LAKE, [TileType.LAKE] * 6)
        t = Tile(TileType.TRAIN, TileType.from_string("TTTPPP"))
        t = Tile(TileType.RIVER, TileType.from_string("RRPPPP"))
        
    
    def test_creation_wrongSideNumber(self):
        with self.assertRaises(AssertionError):
            t = Tile(TileType.PLAINS, [])
            
        with self.assertRaises(AssertionError):
            t = Tile(TileType.PLAINS, [TileType.PLAINS] * 5)
            
        with self.assertRaises(AssertionError):
            t = Tile(TileType.PLAINS, [TileType.PLAINS] * 7)
            
            
    def test_creation_usingRiver(self):
        t = Tile(TileType.RIVER, [TileType.RIVER] * 6)
        t = Tile(TileType.RIVER, TileType.from_string("RRPPPP"))

        # if the center tile is not river, wouldn't 1 river be ok for the side?

        # with self.assertRaises(AssertionError):
        #     t = Tile(TileType.PLAINS, TileType.from_string("RPPPPP"))
            
        with self.assertRaises(AssertionError):
            t = Tile(TileType.RIVER, TileType.from_string("RPPPPP"))
            
            
    def test_creation_usingWater(self):
        t = Tile(TileType.LAKE, [TileType.LAKE] * 6)
        t = Tile(TileType.LAKE, TileType.from_string("LPPPPP"))
        
        with self.assertRaises(AssertionError):
            t = Tile(TileType.PLAINS, [TileType.LAKE] * 6)
            
            
    def test_creation_usingTrain(self):
        t = Tile(TileType.TRAIN, [TileType.TRAIN] * 6)
        t = Tile(TileType.TRAIN, TileType.from_string("TPPPPP"))
        
        with self.assertRaises(AssertionError):
            t = Tile(TileType.PLAINS, [TileType.TRAIN] * 6)
    

class InterfaceTestCase(TestCase):

    def setUp(self):
        self.blankTile = Tile(TileType.PLAINS, [TileType.PLAINS] * 6)
        self.riverTile = Tile(TileType.RIVER, TileType.from_string("RPRPPP"))
        self.medleyTile = Tile(TileType.PLAINS, TileType.from_string("PWHFHW"))
    
    
    def test_get_type(self):
        self.assertEqual(self.blankTile.get_type(), TileType.PLAINS)
        self.assertEqual(self.riverTile.get_type(), TileType.RIVER)
        
        
    def test_get_sides_normal(self):
        self.assertEqual(
                self.blankTile.get_sides(), [TileType.PLAINS] * 6)
        self.assertEqual(
                self.riverTile.get_sides(), TileType.from_string("RPRPPP"))
        self.assertEqual(
                self.medleyTile.get_sides(), TileType.from_string("PWHFHW"))
        
        
    def test_set_rotation_normal(self):
        self.medleyTile.set_rotation(0)
        self.assertEqual(
                self.medleyTile.get_sides(), TileType.from_string("PWHFHW"))
        
        self.medleyTile.set_rotation(1)
        self.assertEqual(
                self.medleyTile.get_sides(), TileType.from_string("WHFHWP"))
        
        self.medleyTile.set_rotation(3)
        self.assertEqual(
                self.medleyTile.get_sides(), TileType.from_string("FHWPWH"))
                
                
    def test_set_rotation_overrotate(self):
        self.medleyTile.set_rotation(6)
        self.assertEqual(
                self.medleyTile.get_sides(), TileType.from_string("PWHFHW"))
                
        self.medleyTile.set_rotation(-3)
        self.assertEqual(
                self.medleyTile.get_sides(), TileType.from_string("FHWPWH"))
                
        self.medleyTile.set_rotation(8)
        self.assertEqual(
                self.medleyTile.get_sides(), TileType.from_string("HFHWPW"))
                
                
    def test_get_sides_ignorerotation(self):
        self.riverTile.set_rotation(3)
        self.assertEqual(
            self.riverTile.get_sides(userotation=False),
            TileType.from_string("RPRPPP")
        )