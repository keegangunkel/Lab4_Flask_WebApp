import unittest
import cone

class coneTest(unittest.TestCase):
    
    #tests that pass
    def test_volume1(self):
        assert(cone.volume(5,10) ==  261.79938779914943)


    def test_surfaceArea(self):
        assert(cone.surfaceArea(5,10) == 254.160184615763)




if __name__ == '__main__':
    unittest.main()