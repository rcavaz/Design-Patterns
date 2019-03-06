#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


"""
ITERATOR
Use the iterator pattern:
    1. to access an aggregate object's contents without exposing internal
       representation.
    2. to support multiple traversals of aggregate objects.
    3. to provide a uniform interface for traversing different aggregate
       structures.
"""


class Iterator(ABC):
    """
    Defines an interface for accessing and traversing elements.
    """
    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def isDone(self):
        pass

    @abstractmethod
    def currentItem(self):
        pass


class ConcreteIterator(Iterator):
    """
    1. Implements the Iterator interface.
    2. Keeps track of the current position in the traversal of the aggregate.
    """

    def __init__(self, obj):
        self.aggregate = obj

    def first(self): pass

    def next(self): pass

    def isDone(self): pass

    def currentItem(self): pass


class Aggregate(ABC):
    """
    Defines an interface for creating an Iterator object.
    """
    @abstractmethod
    def createIterator(self):
        pass


class ConcreteAggregate(Aggregate):
    """
    Implements the Iterator creation interface to return an instance of the
    proper ConcreteIterator.
    """

    def createIterator(self):
        return ConcreteIterator(self)


if __name__ == '__main__':
    unittest.main()
