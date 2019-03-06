#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import logging
import os
import unittest

class Iterator:

    def __init__(self, node):
        self.first = node
        self.start = True
        self.current = None

    def __next__(self):
        if self.start:
            self.current = self.first
            self.start = False
        else:
            self.current = next(self.current)

        if self.isDone():
            raise StopIteration
        else:
            logging.info(f'({self}) next() = {self.current.value}')
            return self.current

    def __str__(self):
        return type(self).__name__

    def isDone(self):
        return self.current is None


class Node:
    def __init__(self, value):
        self.value = value
        self.__child = None

    def __iter__(self):
        return Iterator(self)

    def __next__(self):
        return self.child

    def __str__(self):
        return type(self).__name__

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, node):
        assert(isinstance(node, Node))
        self.__child = node

    def add(self, node):
        logging.debug(f'({self})[{self.value}] add({node.value})')
        if self.child:
            self.child.add(node)
        else:
            self.child = node


class TestIterator(unittest.TestCase):
    def setUp(self):
        logging.info('================== Test Case Set Up ==================')
        self.LinkedList = Node(0)
        for n in range(1, 5):
            self.LinkedList.add(Node(n))

    def test_1(self):
        logging.info('--- Test 1 -------------------------------------------')
        i = 0
        expected = [0, 1, 2, 3, 4]
        for elem in self.LinkedList:
            self.assertEqual(elem.value, expected[i])
            i += 1


if __name__ == '__main__':
    loglevel = 'CRITICAL'
    for lvl in ['ERROR', 'WARNING', 'INFO', 'DEBUG']:
        if os.environ.get(lvl):
            loglevel = lvl
    levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    logging.basicConfig(
        level=levels.get(loglevel),
        format='[%(levelname)s] %(message)s')
    unittest.main()
