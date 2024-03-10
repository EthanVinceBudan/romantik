from enum import Enum

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
        

class Tile:
    def __init__(self, mainType, sideTypes, rotation=0):
        assert(self.__has_valid_layout(mainType,sideTypes))
        self.__rotation = rotation
        self.__center = mainType
        self.__sides = sideTypes
        
        
    # checks if tile can be constructed given the selected main/side types
    def __has_valid_layout(self, mainType, sideTypes):
        # first, ensure exactly six sides
        if len(sideTypes) != 6:
            return False
        # check specific rules
        # - river tiles must flow from edge to middle to edge
        # - train tiles must have at least one edge connection
        # - water tiles are similar to train tiles
        # - river, train and water sides are only valid on tiles which share
        #   a matching main type
        if mainType == TileType.RIVER:
            if sideTypes.count(TileType.RIVER) < 2:
                return False
        elif mainType == TileType.TRAIN:
            if TileType.TRAIN not in sideTypes:
                return False
        elif mainType == TileType.LAKE:
            if TileType.LAKE not in sideTypes:
                return False
        else:
            return not any(i in sideTypes for i in
                    [TileType.RIVER, TileType.LAKE, TileType.TRAIN])
        return True
        
        
    # gets tile sides adjusted for rotation value
    def get_sides(self, userotation=True):
        if userotation:
            return self.__sides[self.__rotation:] + self.__sides[:self.__rotation]
        return self.__sides
        
        
    def get_type(self):
        return self.__center
        
    
    def set_rotation(self,n):
        self.__rotation = n % 6
        
        
    def __str__(self):
        return f"<Tile object: {self.__center} {self.get_sides()}>"