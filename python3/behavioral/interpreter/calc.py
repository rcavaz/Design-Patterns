#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import logging
import os
import re
import unittest


class AbstractExpression(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def interpret(self):
        pass

    def __str__(self):
        return type(self).__name__


class NumericExpression(AbstractExpression):

    def __init__(self, value):
        logging.debug(f'New {self}: {value}')
        self.__value = int(value)

    def interpret(self):
        logging.info(f'({self}) interpret()')
        return self.__value


class MathExpression(AbstractExpression):

    def __init__(self, a, b):
        logging.debug(f'New {self}')
        self.a = a
        self.b = b


class DivideExpression(MathExpression):

    def interpret(self):
        logging.info(f'({self}) interpret()')
        return self.a.interpret() / self.b.interpret()


class MultiplyExpression(MathExpression):

    def interpret(self):
        logging.debug(f'({self}) interpret()')
        return self.a.interpret() * self.b.interpret()


class SubstractExpression(MathExpression):

    def interpret(self):
        logging.debug(f'({self}) interpret()')
        return self.a.interpret() - self.b.interpret()


class SumExpression(MathExpression):

    def interpret(self):
        logging.debug(f'({self}) interpret()')
        return self.a.interpret() + self.b.interpret()


class Context(object):

    def __init__(self, expression):
        logging.debug(f'New {self}: {expression}')
        self.input = expression
        self.output = re.findall(r'(?:[0-9]+)|(?:\*|/|\+|-|\(|\))', expression)
        logging.info(f'({self}) expression: {self.output}')

    def __str__(self):
        return type(self).__name__

    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, value):
        self.__input = value

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        self.__output = value


class Client(object):
    def __init__(self, expression):
        logging.debug(f'New {self}')
        self.__context = Context(expression)
        self.__parse_numbers()
        self.__parse_operations()

    def __str__(self):
        return type(self).__name__

    def __parse_numbers(self):
        logging.info(f'({self}) parse_numbers()')
        c = self.__context.output
        for i in range(0, len(c)):
            try:
                c[i] = NumericExpression(c[i])
            except TypeError:
                pass
            except ValueError:
                pass

    def __parse_operations(self):
        logging.info(f'({self}) parse_operations()')
        c = self.__context.output
        while True:
            try:
                i = c.index('(')
                j = 0
                while i < len(c):
                    if c[i] == '(':
                        j = i
                    elif c[i] == ')':
                        c[j] = self.__build_tree(c[j+1:i])
                        del c[j+1:i+1]
                        break
                    i += 1
            except:
                c = self.__build_tree(c)
                break

    def __build_tree(self, context):
        logging.info(f'({self}) build_tree({context})')
        operations = {
            '/': DivideExpression,
            '*': MultiplyExpression,
            '-': SubstractExpression,
            '+': SumExpression
        }
        for op in ['*','/','+','-']:
            try:
                while len(context) > 1:
                    i = context.index(op)
                    a, b = i-1, i+1
                    context[a] = operations[op](context[a], context[b])
                    del context[i:i+2]
                    logging.info(f'({self}) context: {context}')
            except ValueError:
                pass
        return context[0]

    @property
    def tree(self):
        return self.__context.output[0]

    def solve(self):
        logging.info(f'({self}) solve()')
        return self.__context.output[0].interpret()


class TestCalculator(unittest.TestCase):

    def test_1(self):
        logging.info('--- Test 1 -------------------------------------------')
        string = '1+2+3'
        c = Client(string)
        self.assertTrue(isinstance(c.tree, SumExpression))
        self.assertEqual(c.solve(), 6)

    def test_2(self):
        logging.info('--- Test 2 -------------------------------------------')
        string = '(1+2)*3'
        c = Client(string)
        self.assertTrue(isinstance(c.tree, MultiplyExpression))
        self.assertTrue(isinstance(c.tree.b, NumericExpression))
        self.assertTrue(isinstance(c.tree.a, SumExpression))
        self.assertTrue(isinstance(c.tree.a.a, NumericExpression))
        self.assertTrue(isinstance(c.tree.a.b, NumericExpression))
        self.assertEqual(c.solve(), 9)


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
