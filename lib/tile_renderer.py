from __future__ import annotations
from lib.board import BoardNode
from lib.tile import Tile
from lib.tile_settings import tile_settings, TileType
from lib.cubecoordinate import CubeCoordinate
import pygame

SIDE_WIDTH = 16


class TileRenderer:
    tile: Tile
    name: str
    _screen: pygame.Surface
    colors: list[tuple[int, int, int]]
    vertices: list[list[tuple[int, int]]]
    radius: int
    position: tuple[int, int]

    def __init__(self, screen: pygame.surface, tile: Tile, position: tuple[int, int], radius: int) -> None:
        self._screen = screen
        self.name = tile_settings[tile.get_type()].name
        self.tile = tile
        self.position = position
        self.radius = radius
        self.colors = [tile_settings[tile.get_type()].color] + \
            [tile_settings[t].color for t in tile.get_sides()]

        outer = CubeCoordinate(0, 0, 0).get_vertices(
            position, self.radius, 4)

        inner = CubeCoordinate(0, 0, 0).get_vertices(
            position, self.radius, 4 + SIDE_WIDTH)

        self.vertices = [inner]

        # draw the side polygons
        for i in range(4, 10):
            self.vertices.append((
                inner[i % 6], outer[i % 6], outer[(i+1) % 6], inner[(i+1) % 6]
            ))

    def render(self):
        for i, polygon in enumerate(self.vertices):
            pygame.draw.polygon(
                self._screen, self.colors[i], polygon, 0)
