import unittest
import cylinder

class cylinderTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(cylinder.volume(10,32) == 10053.096491487338)

    def test_surfaceArea(self):
        assert(cylinder.surfaceArea(5,10) == 471.23889803846896)

    #failing test
    #def test_volume3(self):
        #assert(cylinder.volume(10,1000) == 0)


if __name__ == '__main__':
    unittest.main()
