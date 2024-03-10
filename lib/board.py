from lib.tile import Tile, TileType
from lib.cubecoordinate import CubeCoordinate

class BoardNode:
    
    def __init__(self, cubecoord, tile=None):
        self.__tile = tile
        self.__location = cubecoord
        self.__neighbors = [None] * 6
        
        
    def get_location(self):
        return self.__location
        
        
    def set_tile(self,tile):
        self.__tile = tile
        
        
    def get_tile(self):
        return self.__tile
        
        
    def has_tile(self):
        return self.__tile != None
        
        
    def get_neighbors(self, side=None):
        if side != None:
            return self.__neighbors[side%6]
        return self.__neighbors
        
        
    def set_neighbor(self,side,node):
        self.__neighbors[side%6] = node
        
        
    def __str__(self):
        if self.has_tile():
            return f"<Full BoardNode at {self.__location}>"
        return f"<Empty BoardNode at {self.__location}>"
        
        
    def __repr__(self):
        return str(self)
        

class Board:
    
    def __init__(self):
        self.__build_new_board()
        self.__edgeNodes = self.__rootNode.get_neighbors()
        
        
    def __build_new_board(self):
        self.__rootNode = BoardNode(
            CubeCoordinate(0,0,0),
            tile=Tile(TileType.PLAINS, [TileType.PLAINS] * 6)
        )
        self.__allNodes = set([self.__rootNode])
        for i in range(6):
            newNode = BoardNode(self.__rootNode.get_location().adjacent(i))
            self.__allNodes.add(newNode)
            # get nodes adjacent to new one
            ccwNeighbor = self.__rootNode.get_neighbors(side=i-1)
            cwNeighbor = self.__rootNode.get_neighbors(side=i+1)
            # bi-directional connection
            self.__rootNode.set_neighbor(i,newNode)
            newNode.set_neighbor(i+3,self.__rootNode)
            # make auxillary connections if possible
            if ccwNeighbor != None:
                newNode.set_neighbor(i+3+1,ccwNeighbor)
                ccwNeighbor.set_neighbor(i+3-2,newNode)
            if cwNeighbor != None:
                newNode.set_neighbor(i+3-1,cwNeighbor)
                cwNeighbor.set_neighbor(i+3+1,newNode)
        
        
    def edge_nodes(self):
        return self.__edgeNodes
        
        
    def size(self):
        return len(self.__allNodes)
        
        
    def all_nodes(self):
        return self.__allNodes
        
        
    def __str__(self):
        return f"<Board object: {len(self.__edgeNodes)} edge nodes>"