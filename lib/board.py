from __future__ import annotations
from lib.tile import Tile, TileType
from lib.cubecoordinate import CubeCoordinate
from lib.util import opposite

class BoardNode:
    _tile: Tile | None
    _location: CubeCoordinate
    _neighbors: list[BoardNode | None]

    
    def __init__(self, cubecoord, tile=None):
        self._tile = tile
        self._location = cubecoord
        self._neighbors = [None] * 6
        
        
    def get_location(self):
        return self._location
        
        
    def set_tile(self,tile):
        self._tile = tile
        
        
    def get_tile(self):
        return self._tile
        
        
    def has_tile(self):
        return self._tile != None
        
    def get_neighbors(self) -> list[BoardNode | None]:
        return self._neighbors

    def get_neighbor(self, side: int) -> BoardNode | None:
        return self._neighbors[side % 6]
        
    def set_neighbor(self, side: int, node: BoardNode | None) -> None:
        self._neighbors[side % 6] = node

    def is_border(self) -> bool:
        """Returns true if this node is on the outer perimeter of the board"""
        return None in self._neighbors

        
    def __str__(self):
        if self.has_tile():
            return f"<Full BoardNode at {self._location}>"
        return f"<Empty BoardNode at {self._location}>"
        
        
    def __repr__(self):
        return str(self)
        

class Board:
    _positions: dict[CubeCoordinate: BoardNode]
    _border_coords: set[CubeCoordinate]

    def __init__(self):
        self._positions = {}
        self._border_coords = set()
        self._build_new_board()

    def _build_new_board(self):
        origin = BoardNode(CubeCoordinate(0, 0, 0),
                           tile=Tile(TileType.PLAINS, [TileType.PLAINS] * 6))
        self._positions[origin.get_location()] = origin
        self.expand(origin.get_location())

    def expand(self, location: CubeCoordinate) -> int:
        """Create tiles on available sides around source tile and forms all
        valid neighbor connections.

        Returns number of tiles created
        """
        if location not in self._positions:
            raise ValueError(
                f"No tile found at location: {location}")

        node = self._positions[location]
        self._border_coords.discard(location)
        created_count = 0
        for i, neighbor in enumerate(node._neighbors):
            if not neighbor:
                # create a new neighbor and form link if slot is empty
                new_node = BoardNode(location.adjacent(i), None)
                self._positions[new_node.get_location()] = new_node
                node._neighbors[i] = new_node

                # search existing nodes and form new two way connections
                for j in range(6):
                    pos = new_node.get_location().adjacent(j)
                    if pos in self._positions:
                        existing_node = self._positions[pos]
                        new_node.set_neighbor(j, existing_node)
                        existing_node.set_neighbor(opposite(j), new_node)
                        if not existing_node.is_border():
                            self._border_coords.discard(
                                existing_node.get_location())
                    if new_node.is_border():
                        self._border_coords.add(new_node.get_location())
                created_count += 1
        return created_count

    def border_nodes(self):
        return [self._positions[c] for c in self._border_coords]

        
    size = property(fget = lambda s: len(s._positions))
    
        
    def all_nodes(self) -> list[BoardNode]:
        return list(self._positions.values())

        
    def __str__(self):
        return f"<Board object: {len(self._border_coords)} edge nodes>"
