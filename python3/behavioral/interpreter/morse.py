#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import logging
import os
import re
import unittest


class Context(object):

    def __init__(self, abc='', morse=''):
        self.__morse = morse
        self.__abc = abc

    @property
    def morse(self):
        return self.__morse

    @morse.setter
    def morse(self, string):
        self.__morse = string

    @property
    def abc(self):
        return self.__abc

    @abc.setter
    def abc(self, string):
        self.__abc = string


class MorseEncoder(object):
    """
    A recursive iterator that traverses the Morse Abstract Syntax Tree and
    returns a morse sequence which represents the path to a given character.
    (i.e. Will return .- for A, .-.- for C, and None if not found.)
    """
    def __init__(self, root):
        self.__root = root

    def encode(
        self,
        char,
        node=None,
        seq='',
    ):
        if node is None:
            node = self.__root

        if ' ' == char:
            return ' '
        elif node.char == char:
            return seq

        if node.left.char != '<?>':
            newseq = seq + '.'
            left = self.encode(char, node=node.left, seq=newseq)
        else:
            left = None

        if node.right.char != '<?>':
            newseq = seq + '-'
            right = self.encode(char, node=node.right, seq=newseq)
        else:
            right = None

        return left or right


class AbstractExpression(ABC):

    @abstractmethod
    def char(self):
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass

    def interpret_morse(self, context):
        if len(context.morse) == 0:
            context.abc = context.abc + self.char
            return

        # Word separator
        if re.match('   ', context.morse):
            context.morse = context.morse[2:]
            context.abc = context.abc + self.char
            return

        # Character separator
        if re.match(' ', context.morse):
            context.morse = context.morse[1:]
            context.abc = context.abc + self.char
            return

        # Dot / Left
        if re.match(r'\.', context.morse):
            context.morse = context.morse[1:]
            self.left.interpret_morse(context)
            return

        # Dash / Right
        if re.match('-', context.morse):
            context.morse = context.morse[1:]
            self.right.interpret_morse(context)
            return

        raise Exception('Syntax error')

    def interpret_abc(self, context):
        encoder = self.createEncoder()
        morse = encoder.encode(context.abc[0])
        try:
            context.abc = context.abc[1:]
            context.morse += morse
            if len(context.abc) > 0:
                context.morse += ' '
        except BaseException:
            raise Exception('Syntax error')

    def createEncoder(self):
        return MorseEncoder(self)


class TerminalExpression(AbstractExpression):

    def __init__(self, char='<?>'):
        self.__char = char

    @property
    def char(self):
        return self.__char

    @property
    def left(self):
        return self

    @property
    def right(self):
        return self


class NonTerminalExpression(AbstractExpression):

    def __init__(self, **args):
        self.left = (args['dot'] if 'dot' in args else TerminalExpression())
        self.right = (args['dash'] if 'dash' in args else TerminalExpression())
        self.char = (args['char'] if 'char' in args else TerminalExpression())

    @property
    def char(self):
        return self.__char.char

    @char.setter
    def char(self, node=None):
        self.__char = node

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node=None):
        self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node=None):
        self.__right = node


class MorseClient(object):

    def __init__(self):
        # Build the abstract syntax tree
        #
        #   H   V   F   ?   L   ?   P   J   B   X   C   Y   Z   Q   ?   ?
        #    \ /     \ /     \ /     \ /     \ /     \ /     \ /     \ /
        #     S       U       R       W       D       K       G       O
        #      \.   _/         \.   _/         \.   _/         \.   _/
        #        \ /             \ /             \ /             \ /
        #         I               A               N               M
        #          \.....   _____/                 \.....   _____/
        #                \ /                             \ /
        #                 E                               T
        #                  \.............   _____________/
        #                                \ /
        #                               blank
        a = TerminalExpression('A')
        b = TerminalExpression('B')
        c = TerminalExpression('C')
        d = TerminalExpression('D')
        e = TerminalExpression('E')
        f = TerminalExpression('F')
        g = TerminalExpression('G')
        h = TerminalExpression('H')
        i = TerminalExpression('I')
        j = TerminalExpression('J')
        k = TerminalExpression('K')
        l = TerminalExpression('L')
        m = TerminalExpression('M')
        n = TerminalExpression('N')
        o = TerminalExpression('O')
        p = TerminalExpression('P')
        q = TerminalExpression('Q')
        r = TerminalExpression('R')
        s = TerminalExpression('S')
        t = TerminalExpression('T')
        u = TerminalExpression('U')
        v = TerminalExpression('V')
        w = TerminalExpression('W')
        x = TerminalExpression('X')
        y = TerminalExpression('Y')
        z = TerminalExpression('Z')
        # null = TerminalExpression('<?>')
        blank = TerminalExpression(' ')

        # n30 = NonTerminalExpression()
        # n29 = NonTerminalExpression()
        n28 = NonTerminalExpression(char=q)
        n27 = NonTerminalExpression(char=z)
        n26 = NonTerminalExpression(char=y)
        n25 = NonTerminalExpression(char=c)
        n24 = NonTerminalExpression(char=x)
        n23 = NonTerminalExpression(char=b)
        n22 = NonTerminalExpression(char=j)
        n21 = NonTerminalExpression(char=p)
        # n20 = NonTerminalExpression()
        n19 = NonTerminalExpression(char=l)
        # n18 = NonTerminalExpression()
        n17 = NonTerminalExpression(char=f)
        n16 = NonTerminalExpression(char=v)
        n15 = NonTerminalExpression(char=h)
        n14 = NonTerminalExpression(char=o)
        n13 = NonTerminalExpression(char=g, dot=n27, dash=n28)
        n12 = NonTerminalExpression(char=k, dot=n25, dash=n26)
        n11 = NonTerminalExpression(char=d, dot=n23, dash=n24)
        n10 = NonTerminalExpression(char=w, dot=n21, dash=n22)
        n9 = NonTerminalExpression(char=r, dot=n19)
        n8 = NonTerminalExpression(char=u, dot=n17)
        n7 = NonTerminalExpression(char=s, dot=n15, dash=n16)
        n6 = NonTerminalExpression(char=m, dot=n13, dash=n14)
        n5 = NonTerminalExpression(char=n, dot=n11, dash=n12)
        n4 = NonTerminalExpression(char=a, dot=n9, dash=n10)
        n3 = NonTerminalExpression(char=i, dot=n7, dash=n8)
        n2 = NonTerminalExpression(char=t, dot=n5, dash=n6)
        n1 = NonTerminalExpression(char=e, dot=n3, dash=n4)
        self.__root = NonTerminalExpression(char=blank, dot=n1, dash=n2)

    def decode(self, message):
        context = Context(morse=message)

        while len(context.morse) > 0:
            self.__root.interpret_morse(context)

        return context.abc

    def encode(self, message):
        context = Context(abc=message)

        while len(context.abc) > 0:
            self.__root.interpret_abc(context)

        return context.morse


class TestMorseInterpreter(unittest.TestCase):

    def test_1(self):
        message = '... --- ...'
        morse = MorseClient()
        self.assertEqual(morse.decode(message), 'SOS')

    def test_2(self):
        message = '-.- .-   -.. .   .-. -.-. .- ...- .- --..'
        morse = MorseClient()
        self.assertEqual(morse.decode(message), 'KA DE RCAVAZ')

    def test_3(self):
        message = 'SOS'
        morse = MorseClient()
        self.assertEqual(morse.encode(message), '... --- ...')

    def test_4(self):
        message = 'KA DE RCAVAZ'
        morse = MorseClient()
        self.assertEqual(morse.encode(message),
                         '-.- .-   -.. .   .-. -.-. .- ...- .- --..')


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
