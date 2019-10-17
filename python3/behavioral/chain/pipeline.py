# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from logging import basicConfig, info, warning, INFO
from unittest import TestCase, main


import re


class Handler(ABC):

    @abstractmethod
    def handle_request(self):
        pass

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, obj):
        self.__successor = obj


class DecimalConverter(Handler):

    def __init__(self, prefix, base):
        assert isinstance(prefix, str), 'prefix is not a string'
        assert isinstance(base, int), 'base is not a string'
        self.prefix = prefix
        self.base = base
        self.successor = None

    def  handle_request(self, request):
        assert isinstance(request, str)
        if re.match(f'^{self.prefix}', request):
            info(f'Matched {request} as a base {self.base} number')
            return int(request, self.base)
        elif self.successor is not None:
            warning(f'Could not match {request} as a base {self.base}')
            return self.successor.handle_request(request)
        else:
            raise RuntimeError(f'Unknown Positional Number System: {request}')


class TestPipeline(TestCase):

    def setUp(self):
        # Declare a chain of handlers to first attempt converting into binary,
        # then octal and finally hexadecimal.
        hex2int = DecimalConverter('0x', 16)
        oct2int = DecimalConverter('0o', 8)
        bin2int = DecimalConverter('0b', 2)
        oct2int.successor = hex2int
        bin2int.successor = oct2int
        self.converter = bin2int

    def test_bin2int(self):
        num = bin(42)
        self.assertEqual(self.converter.handle_request(num), 42)

    def test_oct2int(self):
        num = oct(42)
        self.assertEqual(self.converter.handle_request(num), 42)

    def test_hex2int(self):
        num = hex(42)
        self.assertEqual(self.converter.handle_request(num), 42)

    def test_exception(self):
        num = '0p9Hx7$'
        with self.assertRaises(RuntimeError):
            self.converter.handle_request(num)


if __name__ == '__main__':
    basicConfig(
        level=INFO,
        format='[%(levelname)s] %(message)s')
    main()
