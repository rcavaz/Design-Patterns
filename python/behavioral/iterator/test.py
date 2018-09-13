import logging
import unittest


class Element(object):

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    def __eq__(self, other):
        return self.value == other.value

    def __ge__(self, other):
        return self > other or self == other

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self < other or self == other

    def __ne__(self, other):
        return self.value != other.value

    def __str__(self):
        return str(self.value)


class TestElement(unittest.TestCase):

    def setUp(self):
        self.a = Element(1)
        self.b = Element(1)
        self.c = Element(2)

    def test_eq(self):
        self.assertTrue(self.a == self.a)
        self.assertTrue(self.a == self.b)
        self.assertFalse(self.a == self.c)

    def test_ge(self):
        self.assertTrue(self.a >= self.a)
        self.assertTrue(self.a >= self.b)
        self.assertTrue(self.c >= self.b)
        self.assertFalse(self.a >= self.c)
        self.assertFalse(self.b >= self.c)

    def test_gt(self):
        self.assertTrue(self.c > self.b)
        self.assertFalse(self.a > self.a)
        self.assertFalse(self.a > self.b)

    def test_lt(self):
        self.assertTrue(self.a < self.c)
        self.assertFalse(self.a < self.a)
        self.assertFalse(self.a < self.b)

    def test_le(self):
        self.assertTrue(self.a <= self.a)
        self.assertTrue(self.a <= self.b)
        self.assertTrue(self.a <= self.c)
        self.assertFalse(self.c <= self.a)
        self.assertFalse(self.c <= self.b)

    def test_ne(self):
        self.assertTrue(self.a != self.c)
        self.assertTrue(self.b != self.c)
        self.assertFalse(self.a != self.a)
        self.assertFalse(self.a != self.b)
        self.assertFalse(self.b != self.b)


if __name__ == '__main__':
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)
    unittest.main()
