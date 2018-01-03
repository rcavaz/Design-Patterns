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
"""
class Drink(object):
    """
    Prototype
    Declares an interface for cloning itself.
    """
    size = 11.2

    def clone(self, **attrs):
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class BeerPrototype(object):
    """
    ConcretePrototype
    Implements an operation for cloning itself.
    """

    def __init__(self):
        self._objects = {}

    def get_objects(self):
        return self._objects

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]


if __name__ == '__main__':
    """
    Client
    Creates a new object by asking a prototype to clone itself.
    """
    dispatcher = BeerPrototype()
    prototype  = Drink()

    g = prototype.clone()
    h = prototype.clone(size=24, foo='bar')
    s = prototype.clone(size=22, bar='biz')
    dispatcher.register('Guiness',  g)
    dispatcher.register('Heineken', h)
    dispatcher.register('Sapporo',  s)

    for n, p in dispatcher.get_objects().items():
        print "%8s: %s" % (n, p.size)

