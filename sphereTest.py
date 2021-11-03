import unittest
import sphere

class sphereTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(sphere.volume(5) ==  523.5987755982989)


    def test_surfaceArea(self):
        assert(sphere.surfaceArea(5) == 314.1592653589793)





if __name__ == '__main__':
    unittest.main()