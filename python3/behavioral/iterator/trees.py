#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import logging
import os
import unittest


class Iterator(ABC):

    @abstractmethod
    def first(): pass

    @abstractmethod
    def next(): pass

    @abstractmethod
    def isDone(): pass

    @abstractmethod
    def currentItem(): pass


class InOrderIterator(Iterator):

    def __init__(self, obj):
        assert(isinstance(obj, Aggregate))
        self.aggregate = obj
        self.current = None
        self.count = 0
        self.stack = list()
        self.__fillStack(obj.root)

    def first(self):
        self.current = None
        self.count = 0
        self.stack = list()
        self.__fillStack(self.aggregate.root)
        return self.next()

    def __fillStack(self, cursor):
        self.stack.append(cursor)
        while cursor is not None and cursor.left:
            cursor = cursor.left
            self.stack.append(cursor)

    def isDone(self):
        if self.count >= len(self.aggregate):
            result = True
        else:
            result = False
        return result

    def next(self):
        if self.isDone():
            self.current = None
        else:
            self.count += 1
            self.current = self.stack.pop()
            if self.current.right:
                self.__fillStack(self.current.right)
        return self.current

    def currentItem(self):
        return self.current


class PreOrderIterator(Iterator):

    def __init__(self, obj):
        assert(isinstance(obj, Aggregate))
        self.aggregate = obj
        self.current = None
        self.count = 0
        self.stack = list()
        self.__fillStack(obj.root)

    def first(self):
        self.current = None
        self.count = 0
        self.stack = list()
        self.__fillStack(self.aggregate.root)
        return self.next()

    def __fillStack(self, cursor):
        if cursor is None:
            return
        if cursor.right:
            self.stack.append(cursor.right)
        if cursor.left:
            self.stack.append(cursor.left)
        self.stack.append(cursor)

    def isDone(self):
        if self.count >= len(self.aggregate):
            result = True
        else:
            result = False
        return result

    def next(self):
        if self.isDone():
            self.current = None
        else:
            self.count += 1
            self.current = self.stack.pop()
            try:
                cursor = self.stack.pop()
                if cursor.right:
                    self.stack.append(cursor.right)
                if cursor.left:
                    self.stack.append(cursor.left)
                self.stack.append(cursor)
            except BaseException:
                pass
        return self.current

    def currentItem(self):
        return self.current


class PostOrderIterator(Iterator):

    def __init__(self, obj):
        assert(isinstance(obj, Aggregate))
        self.aggregate = obj
        self.current = None
        self.count = 0
        self.stack = [obj.root]
        if obj.root:
            self.__fillStack(obj.root.right)
            self.__fillStack(obj.root.left)

    def first(self):
        self.current = None
        self.count = 0
        self.stack = [self.aggregate.root]
        self.__fillStack(self.aggregate.root)
        return self.next()

    def __fillStack(self, cursor):
        if cursor is None:
            return
        self.stack.append(cursor)
        if cursor.right:
            self.__fillStack(cursor.right)
        if cursor.left:
            self.__fillStack(cursor.left)

    def isDone(self):
        if self.count >= len(self.aggregate):
            result = True
        else:
            result = False
        return result

    def next(self):
        if self.isDone():
            self.current = None
        else:
            self.count += 1
            self.current = self.stack.pop()
        return self.current

    def currentItem(self):
        return self.current


class Node(object):

    def __init__(self, value):
        assert(isinstance(value, int))
        self.left = None
        self.right = None
        self.value = value

    def __eq__(self, other):
        assert(isinstance(other, Node))
        return self.value == other.value

    def __gt__(self, other):
        assert(isinstance(other, Node))
        return self.value > other.value

    def __lt__(self, other):
        assert(isinstance(other, Node))
        return self.value < other.value

    def __ge__(self, other):
        assert(isinstance(other, Node))
        return self > other or self == other

    def __le__(self, other):
        assert(isinstance(other, Node))
        return self < other or self == other

    def __ne__(self, other):
        assert(isinstance(other, Node))
        return not self == other

    def addChild(self, node):
        assert(isinstance(node, Node))
        if node < self:
            if self.left is None:
                self.left = node
            else:
                self.left.addChild(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.addChild(node)


class Aggregate(ABC):
    @abstractmethod
    def iterator(): pass


class BinaryTree(Aggregate):

    def __init__(self):
        self.root = None
        self.__nodeCount = 0

    def __len__(self):
        return self.__nodeCount

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            self.root.addChild(node)
        self.__nodeCount += 1

    def iterator(self, name='inorder'):
        iterators = {
            'inorder': InOrderIterator,
            'preorder': PreOrderIterator,
            'postorder': PostOrderIterator
        }
        return iterators[name](self)


class TestNode(unittest.TestCase):

    def setUp(self):
        self.a = Node(1)
        self.b = Node(2)
        self.c = Node(1)

    def test_eq(self):
        self.assertFalse(self.a == self.b)
        self.assertTrue(self.a == self.c)

    def test_ne(self):
        self.assertFalse(self.a != self.c)
        self.assertTrue(self.a != self.b)

    def test_gt(self):
        self.assertFalse(self.a > self.b)
        self.assertTrue(self.b > self.a)

    def test_lt(self):
        self.assertFalse(self.b < self.a)
        self.assertTrue(self.a < self.b)

    def test_ge(self):
        self.assertFalse(self.a >= self.b)
        self.assertTrue(self.b >= self.a)
        self.assertTrue(self.a >= self.a)

    def test_le(self):
        self.assertFalse(self.b <= self.a)
        self.assertTrue(self.a <= self.b)
        self.assertTrue(self.a <= self.a)


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()

    def test_insert_left(self):
        for n in [1, 2]:
            self.tree.insert(n)
        self.assertTrue(len(self.tree) == 2)
        self.assertTrue(self.tree.root.value == 1)
        self.assertTrue(self.tree.root.left is None)
        self.assertTrue(self.tree.root.right.value == 2)

    def test_insert_right(self):
        for n in [2, 1]:
            self.tree.insert(n)
        self.assertTrue(len(self.tree) == 2)
        self.assertTrue(self.tree.root.value == 2)
        self.assertTrue(self.tree.root.right is None)
        self.assertTrue(self.tree.root.left.value == 1)

    def test_iterator_factory(self):
        i = self.tree.iterator('inorder')
        self.assertTrue(isinstance(i, InOrderIterator))
        i = self.tree.iterator('preorder')
        self.assertTrue(isinstance(i, PreOrderIterator))
        i = self.tree.iterator('postorder')
        self.assertTrue(isinstance(i, PostOrderIterator))
        i = self.tree.iterator()
        self.assertTrue(isinstance(i, InOrderIterator))


class TestIterators(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()
        for n in [2, 1, 3]:
            self.tree.insert(n)

    def test_inorder(self):
        i = self.tree.iterator('inorder')
        for n in [1, 2, 3]:
            self.assertEqual(i.next().value, n)
            self.assertEqual(i.currentItem().value, n)
        self.assertTrue(i.isDone())
        self.assertEqual(i.first().value, 1)
        self.assertFalse(i.isDone())

    def test_preorder(self):
        i = self.tree.iterator('preorder')
        for n in [2, 1, 3]:
            self.assertEqual(i.next().value, n)
            self.assertEqual(i.currentItem().value, n)
        self.assertTrue(i.isDone())
        self.assertEqual(i.first().value, 2)
        self.assertFalse(i.isDone())

    def test_postorder(self):
        i = self.tree.iterator('postorder')
        for n in [1, 3, 2]:
            self.assertEqual(i.next().value, n)
            self.assertEqual(i.currentItem().value, n)
        self.assertTrue(i.isDone())
        self.assertEqual(i.first().value, 1)
        self.assertFalse(i.isDone())


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
