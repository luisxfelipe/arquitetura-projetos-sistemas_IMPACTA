import unittest
from square import Square
from circle import Circle
from cube import Cube

class TestAreaCalculator(unittest.TestCase):

    def test_calculate_square_area(self):
        self.assertEqual(Square(20).calculate(), float(400))
        self.assertEqual(Square(35).calculate(), float(1225))
        self.assertEqual(Square(50.89).calculate(), float(2589.79))


    def test_calculate_circle_area(self):
        self.assertEqual(Circle(3).calculate(), float(28.26))
        self.assertEqual(Circle(10).calculate(), float(314.00))
        self.assertEqual(Circle(5001.75).calculate(), float(78554959.62))

    def test_calculate_cube_area(self):
        self.assertEqual(Cube(5).calculate(), float(150))
        self.assertEqual(Cube(20).calculate(), float(2400))
        self.assertEqual(Cube(48.14).calculate(), float(13904.76))

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAreaCalculator)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()

'''
if __name__ == "__main__":
    unittest.main
'''
