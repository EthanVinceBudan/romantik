from __future__ import annotations
import math


def coords_from_xy(xy: tuple[int, int], radius: int = 1) -> CubeCoordinate:
    q = round(xy[0] / (1.5 * radius))
    r = round((xy[1] / (radius * math.sqrt(3)) - 0.5 * q))
    s = - (q + r)
    return CubeCoordinate(q, r, s)

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
    
    def get_vertices(self, offset: tuple[int, int] = (0, 0), r: int = 1,
                     padding: int = 0) -> tuple[tuple[float, float]]:
        """returns x, y converted vertex coordinates scaled by radius r"""
        vertices = [None]*6
        center_x, center_y = self.to_cartesian(r)
        center_x += offset[0]
        center_y += offset[1]
        for i in range(6):
            rad = math.pi / 3 * i
            vertices[i] = (center_x + (r - padding) * math.cos(rad),
                           center_y + (r - padding) * math.sin(rad))
        return vertices

    def to_cartesian(self, r: int = 1) -> tuple[float, float]:
        """returns x, y converted coordinates scaled by radius r"""
        x = 1.5 * self.q
        y = math.sqrt(3) * (self.r + self.q / 2)
        return (x * r, y * r)
     
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