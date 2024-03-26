from __future__ import annotations
import random
from lib.util import opposite
from lib.tile_settings import TileType, tile_settings


class Tile:
    _center: TileType
    _sides: TileType
    _rotation: int
    _max_random_sides: int

    def __init__(self, mainType: TileType, sideTypes: list[TileType] = None, rotation: int = 0):
        # randomly generate sides based on rules if none supplied
        self._max_random_sides = tile_settings[mainType].max_random_sides
        if sideTypes == None:
            sideTypes = self.generate_sides(mainType)
        assert (self._validate_layout(mainType, sideTypes))
        self._center = mainType
        self._sides = sideTypes
        self._rotation = rotation

    def generate_sides(self, mainType: TileType) -> list[TileType]:
        sides = [mainType] * 6
        # randomize some number of the sides
        indices = random.sample(range(6), self._max_random_sides)
        for i in indices:
            sides[i] = random.choice(list(TileType))
        return sides

    # checks if tile can be constructed given the selected main/side types
    def _validate_layout(self, mainType: TileType, sideTypes: list[TileType]) -> bool:
        # first, ensure exactly six sides
        if len(sideTypes) != 6:
            return False
        # check specific rules
        # - river tiles must flow from edge to middle to edge
        # - train tiles must have at least one edge connection
        # - water tiles are similar to train tiles
        # - river, train and water sides are only valid on tiles which share
        #   a matching main type
        if sideTypes.count(mainType) < (6 - self._max_random_sides):
            return False
        return True

    # abstract method for checking placement validity (side matching)
    def _validate_placement(self, neighbors: list[Tile | None]) -> bool:
        for i, neighbor in enumerate(neighbors):
            this = self.get_side(i)
            if neighbor != None:
                other = neighbor.get_side(opposite(i))
                if other != this:
                    if not ((this in tile_settings[other].connection_types
                            or not tile_settings[other].connection_types) and (
                            other in tile_settings[this].connection_types
                            or not tile_settings[this].connection_types)):
                        return False
        return True


    # gets tile sides adjusted for rotation value
    def get_sides(self, userotation=True):
        if userotation:
            return self._sides[self._rotation:] + self._sides[:self._rotation]
        return self._sides

    # gets single tile side adjusted for rotation value
    def get_side(self, idx: int, userotation=True):
        if userotation:
            return self._sides[(idx + self._rotation) % 6]
        return self._sides[idx]
        
    def get_type(self):
        return self._center

    # prob obsolete, replace with rotate
    def set_rotation(self,n):
        self._rotation = n % 6

    def rotate(self, magnitude: int) -> None:
        self._rotation = (self._rotation + magnitude) % 6

    def __str__(self):
        return f"<Tile object: {self._center} {self.get_sides()}>"
