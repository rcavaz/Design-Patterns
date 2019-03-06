#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

"""
INTERPRETER
Use this pattern when there is a language to interpret, and you can represent
statements in the language as abstract syntax trees. The interpreter pattern
works best when:
    1. The grammar is simple. For complex grammars, the class hierarchy for the
       grammar becomes large and unmanageable. Tools such as parse regenerators
       are a better alternative in such cases. they can interpret epxressions
       without building abstract syntax trees, which can save space and
       possible time.
    2. Efficiency is not a critical concern. The most efficient interpreters
       are usually not implemented by interpreting parse trees directly but by
       first translating them into another form. For example, regular
       expressions are often transformed into state machines. But even then,
       the translator can be implemented by the Interpreter pattern, such
       pattern is still applicable.
"""

class AbstractExpression(ABC):
    """
    Declares an abstract Interpret operation that is common to all nodes in
    the abstract syntax tree.
    """
    def __init__(self, expression=None):
        self._expression = expression

    @abstractmethod
    def interpret(self, context):
        pass


class TerminalExpression(AbstractExpression):
    """
    1. Implements an Interpret operation associated with terminal symbols in
       the grammar.
    2. An instance is required for every terminal symbol in a sentence.
    """
    def interpret(self, context):
        pass


class NonTerminalExpression(AbstractExpression):
    """
    1. One such class is required for every rule in the grammar.
    2. Maintains instance variables of type AbstractExpression for each of the
       symbols.
    3. Implements an Interpret operation for nonterminal symbols in the
       grammar. Interpret typically calls itself recursively on the variables
       representing the symbols it maintains.
    """
    def interpret(self, context):
        pass


class Context(object):
    """
    Contains information that's global to the interpreter.
    """
    pass


class Client(object):
    """
    1. Builds (or is given) an abstract syntax tree representing a particular
       sentence in the language that the grammar defines. The abstract tree is
       assembled from instances of the NonterminalExpression and
       TerminalExpression classes.
    2. Invokes the Interpret operation.
    """
    def main(self):
        pass
