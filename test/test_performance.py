from unittest import TestCase
from time import time as now

from lib.tile import Tile, TileType

class ProfileTile(TestCase):

    NUM_TILES = 10_000
    
    def test_tile_creation_performance(self):
        startTime = now()
        for _ in range(ProfileTile.NUM_TILES):
            t = Tile(TileType.PLAINS, TileType.from_string("PPPPPP"))
            self.assertEqual(t.get_sides(), TileType.from_string("PPPPPP"))
        endTime = now()
        print(f"Took {endTime-startTime:.3f}s")