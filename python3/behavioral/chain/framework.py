from abc import ABC, abstractmethod
import logging
import os
import unittest


class Handler(ABC):

    def __init__(self, successor=None):
        logging.debug(f'({type(self).__name__}) Created new instance with id: {id(self)}')
        self.__successor = successor

    @abstractmethod
    def handle_request(self):
        pass

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, obj):
        self.__successor = obj


class Composite(Handler):

    def __init__(self):
        self.__children = list()
        self.__handlers = dict()
        super().__init__()

    @property
    def children(self):
        return self.__children

    def add(self, obj):
        obj.successor = self
        self.__children.append(obj)

    @property
    def handlers(self):
        return self.__handlers

    @handlers.setter
    def handlers(self, handler):
        assert isinstance(handler, tuple)
        name, func = handler
        assert isinstance(name, str), 'Handler name must be a string'
        assert type(func).__name__ == 'function', 'Handler is not a function'
        self.__handlers[name] = func

    def handle_request(self, request):
        logging.debug(f'({id(self)}) Attempting to handle request \'{request.name}\'.')
        try:
            handle = self.handlers[request.name]
            logging.info(f'({id(self)}) Request \'{request.name}\' handled successfully')
            return handle(request)
        except KeyError:
            if self.successor is not None:
                return self.successor.handle_request(request)
            else:
                logging.error(f'({id(self)}) Could not handle request {request.name}')
                return False


class Request:
    pass


class TestChainOfResponsibilities(unittest.TestCase):

    def setUp(self):
        r = Request()
        r.name = 'foo'
        r.data = 'World'
        self.request = r

    def test_1(self):
        logging.info('********** Test Case 1')
        r = self.request
        c = Composite()
        self.assertFalse(c.handle_request(r))

    def test_2(self):
        logging.info('********** Test Case 2')
        r = self.request
        c = Composite()
        c.handlers = ('foo', lambda x: f'Hello, {x.data}!')
        self.assertEqual(c.handle_request(r), 'Hello, World!')

    def test_3(self):
        logging.info('********** Test Case 3')
        r = self.request
        leaf = Composite()
        root = leaf
        for i in range(0, 4):
            tmp = Composite()
            tmp.add(root)
            root = tmp
        root.handlers = ('foo', lambda x: f'{x.name}, bar, baz!')
        self.assertEqual(leaf.handle_request(r), 'foo, bar, baz!')


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
