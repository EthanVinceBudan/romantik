from __future__ import annotations
from lib.tile import Tile
from lib.tile_settings import tile_settings
import random


class Deck:
    _size: int
    _top: Tile | None

    def __init__(self, size: int = 100) -> None:
        self._size = size
        self.flip()

    def flip(self) -> None:
        if self._size > 0:
            self._top = Tile(random.choice(list(tile_settings.keys())))
        else:
            self._top = None

    def peek(self) -> Tile | None:
        return self._top

    def draw(self) -> Tile | None:
        if self._top:
            tile = self._top
            self._size -= 1
            self.flip()
            return tile

    def __len__(self) -> int:
        return self._size
