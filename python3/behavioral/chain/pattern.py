#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import logging
import os
import unittest

"""
Use Chain of Responsibility when:
    - more than one object may handle a request, and the handler isn't known a priori. The handler should be ascertained automatically.
    - you want to issue a request to one of several objects without specifying the receiver explicitly.
    - the set of objects that can handle a request should be specified dynamically.
"""


class Handler(ABC):
    """
    - Defines an interface for handling requests.
    - (optional) implements the successor link.
    """

    def __init__(self, successor=None):
        logging.debug(f'New {self}, successor: {successor}')
        self.successor = successor

    def __str__(self):
        return type(self).__name__

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, new):
        self.__successor = new

    @abstractmethod
    def handle_request(self):
        pass


class ConcreteHandler1(Handler):
    """
    - Handles requests it is responsible for.
    - Can access its successor.
    - If the ConcreteHandler can handle the request, it does so; otherwise it forwards the request to its successor.
    """

    def handle_request(self, handle=False):
        if handle:
            logging.info(f'({self}) Request handled successfully')
            return True
        else:
            logging.info(f'({self}) Could not handle request')
            raise RuntimeError('Unable to handle request')


class ConcreteHandler2(Handler):
    def handle_request(self, handle=False):
        if handle:
            logging.info(f'Request handled by: {self}')
            return True
        elif self.successor is not None:
            logging.info(f'({self}) Request handling chained to \'{self.successor}\'')
            return self.successor.handle_request(handle)
        else:
            return False


class Client(object):
    """
    - Initiates the request to a ConcreteHandler object on the chain.
    """

    def action_1(self, request):
        h = ConcreteHandler1()
        return h.handle_request(request)

    def action_2(self, request):
        h1 = ConcreteHandler1()
        h2 = ConcreteHandler2(h1)
        return h2.handle_request(request)


class TestChainOfResponsibility(unittest.TestCase):
    def setUp(self):
        logging.info('================== Test Case Set Up ==================')
        self.client = Client()
    """
    - When a client issues a request, the request propagates along the chain until a ConcreteHandler object takes responsibility for handling it.
    """

    def test_1(self):
        logging.info('--- Test 1 -------------------------------------------')
        c = self.client
        self.assertTrue(c.action_1(True))

    def test_2(self):
        logging.info('--- Test 2 -------------------------------------------')
        c = self.client
        self.assertTrue(c.action_2(True))

    def test_3(self):
        logging.info('--- Test 3 -------------------------------------------')
        with self.assertRaises(RuntimeError):
            self.client.action_2(False)


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
