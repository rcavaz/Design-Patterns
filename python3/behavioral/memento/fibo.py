import pickle
import unittest


"""
Use the memento pattern to support a 'prev' operation that allows to roll back
to a previous teration state.
"""

class FibonacciIterator:
    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__c = 0

    @property
    def current(self):
        return self.__c

    @property
    def next(self):
        if self.__a == 0 and self.__b == 0:
            self.__b = 1
        else:
            self.__c = self.__a + self.__b
            self.__a = self.__b
            self.__b = self.__c
        return self.__c

    @property
    def memento(self):
        # Here, the vars() function returns the __dict__ attribute of out
        # object and its passed to the pickle module to pack it into a binary
        # stream, thus honoring encapsulation.
        return pickle.dumps(vars(self))

    @memento.setter
    def memento(self, bstream):
        # Unpacks the binary stream into a python object that can be used by
        # vars() to update the object state.
        prev_state = pickle.loads(bstream)
        vars(self).clear()
        vars(self).update(prev_state)


class TestFibonacciIterator(unittest.TestCase):

    def setUp(self):
        self.iterator = FibonacciIterator()

    def test_1(self):
        m = list()
        for _ in range(0, 7):
            m.append(self.iterator.memento)
            self.iterator.next
        self.assertEqual(self.iterator.current, 13)

        for expected in [8, 5, 3]:
            self.iterator.memento = m.pop()
            self.assertEqual(self.iterator.current, expected)


if __name__ == '__main__':
    unittest.main()
