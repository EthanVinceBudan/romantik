from __future__ import annotations
from enum import Enum


class TileSettings:
    name: str
    color: tuple[int, int, int]
    max_random_sides: int
    connection_types: tuple[TileType]  # empty list implies connect to anything

    def __init__(self, name: str, color: tuple[int, int, int],
                 max_random_sides: int, connection_types: tuple[TileType]) -> None:
        self.name = name
        self.color = color
        self.max_random_sides = max_random_sides
        self.connection_types = connection_types


class TileType(Enum):
    PLAINS = "P"
    WOODS = "W"
    HOUSES = "H"
    FIELDS = "F"
    LAKE = "L"
    RIVER = "R"
    TRAIN = "T"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    # creates a list of tiletypes from a string

    def from_string(inputStr):
        result = []
        for c in inputStr:
            result.append(TileType(c))
        return result


tile_settings = {
    TileType.PLAINS: TileSettings("Plains", (134, 196, 63), 5, []),
    TileType.RIVER: TileSettings("River", (50, 130, 209), 4, [TileType.RIVER]),
    TileType.TRAIN: TileSettings("Railroad", (143, 143, 143), 5, [TileType.TRAIN]),
    TileType.LAKE: TileSettings("Lake", (9, 96, 181), 5, [TileType.LAKE]),
    TileType.WOODS: TileSettings("Woods", (35, 87, 33), 4, []),
    TileType.HOUSES: TileSettings("Houses", (87, 82, 76), 6, []),
    TileType.FIELDS: TileSettings("Fields", (224, 216, 63), 4, []),
}
