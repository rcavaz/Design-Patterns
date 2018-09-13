import logging
import unittest


class Iterator(object):
    def first(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def isDone(self):
        raise NotImplementedError

    def currentItem(self):
        raise NotImplementedError


class InOrderIterator(Iterator):
    def __init__(self, obj):
        logging.info('({}) New iterator'.format(type(self).__name__))
        assert(isinstance(obj, Aggregate))
        assert(isinstance(obj.root, Node))
        self.aggregate = obj
        self.current = None
        self.count = 0
        self.stack = list()
    def first(self):
        logging.info('({}) Reset iterator'.format(type(self).__name__))
        self.stack = list()
        self.count = 0
        self.current = None
        self.fillStack()
        return self.next()
    def next(self):
        logging.info('({}) Get next item ...'.format(type(self).__name__))
        if self.isDone():
            return None
        if len(self.stack) == 0:
            self.fillStack()
        self.count += 1
        return self.pop()
    def pop(self):
        self.current = self.stack.pop()
        if self.current.right is not None:
            self.stack.append(self.current.right)
            self.fillStack()
        logging.info('({}) ... current item: {}'.format(type(self).__name__, self.current.value))
        return self.current
    def fillStack(self):
        logging.info('({}) Fill stack'.format(type(self).__name__))
        if self.current is None:
            cursor = self.aggregate.root
            self.stack.append(cursor)
        else:
            cursor = self.stack[-1]
        while cursor.left is not None:
            cursor = cursor.left
            self.stack.append(cursor)
    def isDone(self):
        if self.count >= len(self.aggregate):
            result = True
        else:
            result = False
        logging.info('({}) Done traversing? {}'.format(type(self).__name__, result))
        return result
    def currentItem(self):
        logging.info('({}) Get current item: {}'.format(type(self).__name__, self.current.value))
        return self.current


class PreOrderIterator(Iterator):
    def __init__(self, obj):
        logging.info('({}) New iterator'.format(type(self).__name__))
        assert(isinstance(obj, Aggregate))
        assert(isinstance(obj.root, Node))
        self.aggregate = obj
        self.current = None
        self.count = 0
        self.stack = list()
    def first(self):
        logging.info('({}) Reset iterator'.format(type(self).__name__))
        self.current = None
        self.count = 0
        self.stack = list()
        return self.next()
    def fillStack(self):
        logging.info('({}) Fill stack'.format(type(self).__name__))
        if self.current.right is not None:
            self.stack.append(self.current.right)
        if self.current.left is not None:
            self.stack.append(self.current.left)
    def next(self):
        if self.isDone():
            return None
        elif self.count == 0:
            self.current = self.aggregate.root
        else:
            self.current = self.stack.pop()
        self.fillStack()
        self.count += 1
        logging.info('({}) Get next item: {}'.format(type(self).__name__, self.current.value))
        return self.current
    def isDone(self):
        if self.count >= len(self.aggregate):
            result = True
        else:
            result = False
        logging.info('({}) Done traversing? {}'.format(type(self).__name__, result))
        return result
    def currentItem(self):
        logging.info('({}) Get current item: {}'.format(type(self).__name__, self.current.value))
        return self.current


class Aggregate(object):
    def iterator(self):
        raise NotImplementedError


class Node(object):
    def __init__(self, value):
        assert(isinstance(value, int))
        self.left = None
        self.parent = None
        self.right = None
        self.value = value
    def setParent(self, node):
        self.parent = node
    def addChild(self, node):
        assert(isinstance(node, Node))
        if node.value < self.value:
            if self.left is None:
                self.left = node
                node.setParent(self)
            else:
                self.left.addChild(node)
        else:
            if self.right is None:
                self.right = node
                node.setParent(self)
            else:
                self.right.addChild(node)


class BinaryTree(Aggregate):
    def __init__(self):
        self.root = None
        self.node_count = 0
    def __len__(self):
        return self.node_count
    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            self.root.addChild(node)
        self.node_count += 1
    def iterator(self, kind='inorder'):
        def inorder():
            return InOrderIterator(self)
        def preorder():
            return PreOrderIterator(self)
        def postorder():
            return PostOrderIterator(self)
        kinds = {
            'inorder': inorder
            ,'preorder': preorder
            ,'postorder': postorder
        }
        iterator = kinds[kind]
        return iterator()


class TestIteratorPattern(unittest.TestCase):
    def setUp(self):
        self.obj = BinaryTree()
        for n in [2, 1, 3]:
            self.obj.insert(n)
    def test_in_order(self):
        iterator = self.obj.iterator('inorder')
        for n in [1, 2, 3]:
            self.assertEqual(iterator.next().value, n)
        self.assertEqual(iterator.next(), None)
        self.assertEqual(iterator.first().value, 1)
        self.assertEqual(iterator.next().value, 2)
    def test_pre_order(self):
        iterator = self.obj.iterator('preorder')
        for n in [2, 1, 3]:
            self.assertEqual(iterator.next().value, n)
        self.assertEqual(iterator.next(), None)
        self.assertEqual(iterator.first().value, 2)
        self.assertEqual(iterator.next().value, 1)


if __name__ == '__main__':
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)
    unittest.main()
