class CubeCoordinate:

    ADJACENT_VECTORS = [
        (0,-1,1),
        (1,-1,0),
        (1,0,-1),
        (0,1,-1),
        (-1,1,0),
        (-1,0,1)
    ]
    
    def __init__(self,q,r,s):
        if (q+r+s != 0):
            raise ValueError(f"Coordinates ({q}, {r}, {s}) not valid: must add to 0")
        self.__q = q
        self.__r = r
        self.__s = s
            
            
    q = property(fget=lambda s: s.__q)
    r = property(fget=lambda s: s.__r)
    s = property(fget=lambda s: s.__s)
        
    
    # return new coordinte object adjacent to this one, in the given direction
    def adjacent(self,side):
        side = side%6
        return self + CubeCoordinate(*CubeCoordinate.ADJACENT_VECTORS[side])
    
     
    def __add__(self, cc):
        return CubeCoordinate(self.q + cc.q, self.r + cc.r, self.s + cc.s)
        
        
    def __eq__(self, cc):
        return self.q == cc.q and self.r == cc.r and self.s == cc.s

    def __hash__(self) -> int:
        return hash((self.q, self.r, self.s))

        
    def __str__(self):
        return f"<Cube coordinate ({self.__q}, {self.__r}, {self.__s})>"
        
        
    def __repr__(self):
        return str(self)