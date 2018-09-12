import logging
import unittest


"""
ITERATOR
Use the iterator pattern:
    1. to access an aggregate object's contents without exposing internal
       representation.
    2. to support multiple traversals of aggregate objects.
    3. to provide a uniform interface for traversing different aggregate
       structures.
"""
class Iterator(object):
    """
    Defines an interface for accessing and traversing elements.
    """
    def first(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def isDone(self):
        raise NotImplementedError

    def currentItem(self):
        raise NotImplementedError


class ConcreteIterator(Iterator):
    """
    1. Implements the Iterator interface.
    2. Keeps track of the current position in the traversal of the aggregate.
    """
    def __init__(self, obj):
        logging.info('({}) New iterator'.format(type(self).__name__))
        assert(isinstance(obj, Aggregate))
        self.aggregate = obj
        self.current = None
        self.count = -1

    def first(self):
        logging.info('({}) Reset iterator'.format(type(self).__name__))
        self.count = 0
        self.current = self.aggregate.elements[self.count]
        return self.current

    def next(self):
        if self.isDone():
            logging.info('({}) Is Done'.format(type(self).__name__))
            self.current = None
        else:
            logging.info('({}) Not done yet'.format(type(self).__name__))
            self.count += 1
            self.current = self.aggregate.elements[self.count]
        logging.info('({}) Next element: {}'.format(type(self).__name__, self.current))
        return self.current

    def isDone(self):
        if self.count +1 >= len(self.aggregate):
            result = True
        else:
            result = False
        logging.info('({}) Done traversing? {}'.format(type(self).__name__, result))
        return result

    def currentItem(self):
        logging.info('({}) Get current item: {}'.format(type(self).__name__), self.current)
        return self.current


class Aggregate(object):
    """
    Defines an interface for creating an Iterator object.
    """
    def createIterator(self):
        raise NotImplementedError


class ConcreteAggregate(Aggregate):
    """
    Implements the Iterator creation interface to return an instance of the
    proper ConcreteIterator.
    """
    def __init__(self):
        logging.info('({}) New Aggregate'.format(type(self).__name__))
        self.elements = list()
    def __len__(self):
        return len(self.elements)
    def push(self, element):
        self.elements.append(element)
    def createIterator(self):
        return ConcreteIterator(self)


class TestIteratorPattern(unittest.TestCase):
    def setUp(self):
        self.obj = ConcreteAggregate()
        for i in range(0, 3):
            self.obj.push(i)
        self.iterator = self.obj.createIterator()
    def test_1(self):
        for i in range(0, 3):
            self.assertEquals(self.iterator.next(), i)
        self.assertTrue(self.iterator.isDone())
    def test_2(self):
        for i in range(0, 2):
            self.iterator.next()
        self.assertEquals(self.iterator.first(), 0)


if __name__ == '__main__':
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)
    unittest.main()
