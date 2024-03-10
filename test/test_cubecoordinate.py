from unittest import TestCase

from lib.cubecoordinate import CubeCoordinate

class CreationTestCase(TestCase):
    
    def test_creation_normal(self):
        cc = CubeCoordinate(0,0,0)
        cc = CubeCoordinate(1,-1,0)
        cc = CubeCoordinate(-12,7,5)
        
    
    def test_creation_abnormal(self):
        with self.assertRaises(ValueError):
            cc = CubeCoordinate(0,0,1)
            
        with self.assertRaises(ValueError):
            cc = CubeCoordinate(1,0,0)
            
        with self.assertRaises(ValueError):
            cc = CubeCoordinate(0,1,0)
            
        with self.assertRaises(ValueError):
            cc = CubeCoordinate(-12,7,6)
            
            
class InterfaceTestCase(TestCase):

    def setUp(self):
        self.origin = CubeCoordinate(0,0,0)
        self.adjacentToOrigin = CubeCoordinate(1,0,-1)
        self.small_onaxis = CubeCoordinate(2,-2,0)
        self.small_offaxis = CubeCoordinate(-1,-1,2)
        self.large_onaxis = CubeCoordinate(0,3192,-3192)
        self.large_offaxis = CubeCoordinate(-1284,2236,-952)
    
    
    def test_comparisons(self):
        duplicate_1 = CubeCoordinate(3,-2,-1)
        duplicate_2 = CubeCoordinate(3,-2,-1)
        self.assertEqual(duplicate_1, duplicate_2)
        
        
    def test_addition(self):
        expectedResult = CubeCoordinate(1,-3,2)
        actualResult = self.small_onaxis + self.small_offaxis
        self.assertEqual(actualResult, expectedResult)
        
        
    def test_adjacent_normal(self):
        self.assertEqual(self.origin.adjacent(0), CubeCoordinate(0,-1,1))
        self.assertEqual(self.small_onaxis.adjacent(1), CubeCoordinate(3,-3,0))
        
        
    def test_adjacent_abnormal(self):
        self.assertEqual(self.large_offaxis.adjacent(0),
                self.large_offaxis.adjacent(6))
        self.assertEqual(self.small_offaxis.adjacent(-2), 
                self.small_offaxis.adjacent(10))