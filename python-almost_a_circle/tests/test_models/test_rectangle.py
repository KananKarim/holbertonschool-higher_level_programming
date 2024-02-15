import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_arg1(self):
        # obj = Rectangle(1, 2)
        self.assertEqual(Rectangle(1, 2).width, 1)
        self.assertEqual(Rectangle(1, 2).height, 2)
    def test_arg2(self):
        obj = Rectangle(1, 2, 3)
        self.assertEqual(obj.x, 3)
    def test_arg3(self):
        obj = Rectangle(1, 2, 3, 4)
        self.assertEqual(obj.y, 4)
    def test_arg4(self):
        with self.assertRaises(TypeError) as context:
            obj = Rectangle("1", 2)
        self.assertEqual("width must be an integer", str(context.exception))
    def test_arg5(self):
        with self.assertRaises(TypeError) as context:
            obj = Rectangle(1, "2")
        self.assertEqual("height must be an integer", str(context.exception))
    def test_arg6(self):
        with self.assertRaises(TypeError) as context:
            obj = Rectangle(1, 2, "3")
        self.assertEqual("x must be an integer", str(context.exception))
    def test_arg7(self):
        with self.assertRaises(TypeError) as context:
            obj = Rectangle(1, 2, 3, "4")
        self.assertEqual("y must be an integer", str(context.exception))
    def test_arg8(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
    def test_arg9(self):
        with self.assertRaises(ValueError) as context:
            obj = Rectangle(-1, 2)
        self.assertEqual("width must be > 0", str(context.exception))
    def test_arg10(self):
        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, -2)
        self.assertEqual("height must be > 0", str(context.exception))
    