import unittest
from cube import cube_area


class TestCubeArea(unittest.TestCase):
    def test_cube_area(self):
        self.assertEqual(cube_area(3), 54)

    def test_value(self):
        self.assertRaises(ValueError, cube_area, 0)

    def test_types(self):
        self.assertRaises(TypeError, cube_area, True)
        self.assertRaises(TypeError, cube_area, [0])
        self.assertRaises(TypeError, cube_area, {})
        self.assertRaises(TypeError, cube_area, (1, 2))

# Запустим тест
#$  python -m unittest test_cube.py