#!/usr/bin/env python
"""
PROTOTYPE

Use the Prototype pattern when a system should be independent of how its
products are created, composed, and represented; and:
    1. when the classes to instantiate are specified at run-time.
    2. to avoid building a class hierarchy of factories that parallels the
       class hierarchy of products.
    3. when instances of a class can have one of only a few different
       combinations of state.


Implementation:

    Let's say we have 3 brands of beer but let's pretend they all have share
    the same brewing process and only differ by their brand and can size.
    Brewing is a time consuming task which we don't want to go through more
    than once and instead will clone from it.

    We will create a Prototype class called Drink that will define an cloning
    interface.

    Then we will create a ConcretePrototype class called BeerPrototype which
    will implement the clone interface and will define the Brewing.

    Finally we will create a Client class that will instantiate BeerPrototype
    and clone from it while providing aditional settings to the final product.
"""
import copy
import logging
import time
import sys


class Drink(object):
    """
    Prototype
    Declares an interface for cloning itself.
    """
    def clone(self):
        raise NotImplementedError


class BeerPrototype(Drink):
    """
    ConcretePrototype
    Implements an operation for cloning itself.
    """
    size = 11
    def __init__(self):
        self._objects = {}
        logging.info('Loading instance (brewing) ...')
        # Pretend this to be a costly operation.
        for i in range(0,51):
            sys.stdout.write('\rProgress: %s (%s%s)' % ('.'*i, 2*i, '%'))
            sys.stdout.flush()
            time.sleep(0.02)
        print ''

    def clone(self, **attrs):
        # A shallow copy through copy() will only clone this instance and set
        # references to any other objects that compose it, while a deepcopy()
        # will create a copy of this instance and all other objects that
        # compose it. Either way, the clone won't have to go through the
        # costly initialization.
        logging.info('Cloning prototype ...')
        obj = copy.copy(self)
        obj.__dict__.update(attrs)
        return obj


class Client:
    """
    Client
    Creates a new object by asking a prototype to clone itself.
    """
    def main(self):
        # Prototype has many of the same consequences that AbstractFactory and
        # Builder have: It hides the concrete product classes from the client,
        # thereby reducing the number of names clients know about. Moreover,
        # these patterns let a client work with application-specific classes
        # without modification.
        #
        # Additional benefits of the Prototype pattern are:
        # 1. Adding and removing products at run-time.
        # 2. Specifying new objects by varying values.
        # 3. Specifying new objects by varying structure.
        # 4. Reduced subclassing.
        # 5. Configuring an application with classes dynamically.
        #
        # The main liability of this pattern is that each subclass of Prototype
        # must implement the clone operation, which may be difficult if for
        # example, the classes under consideration already exist.
        # Implementing clone can be difficult when their internals include
        # objects that don't support copying or have circualr references.
        logging.basicConfig(level=logging.INFO)

        prototype = BeerPrototype()
        p1 = prototype.clone()
        p2 = prototype.clone(size=22, foo='bar')
        p3 = p2.clone(size=24)

        # This will be
        objects = {}
        objects['Heineken'] = p1
        objects['Guiness']  = p2
        objects['Sapporo']  = p3

        for n, p in objects.items():
            try:
                print "%8s: %4s - (%s)" % (n, p.size, p.foo)
            except:
                print "%8s: %4s" % (n, p.size)


if __name__ == '__main__':
    client = Client()
    client.main()
