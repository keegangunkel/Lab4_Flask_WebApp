import unittest
import sphere

class sphereTest(unittest.TestCase):

    #tests that pass
    def test_volume1(self):
        assert(sphere.volume(5) ==  523.5987755982989)


    def test_volume2(self):
        assert(sphere.volume(69) == 1376055.2813841724)





if __name__ == '__main__':
    unittest.main()