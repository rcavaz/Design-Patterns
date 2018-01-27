#!/usr/bin/env python
"""
COMPOSITE

Use this pattern when:
    1. you want to represent part-whole hierarchies of objects.
    2. you want clients to be able to ignore the difference between
       compositions of objects and individual objects. Clients will treat all
       objects in the composite structure uniformly.
"""
class Component(object):
    """
    1. Declares the interface for objects in the composition.
    2. Implements default behavior for the interface common to all classes as
       appropriate.
    3. Declares an interface for accessing and managing its child components.
    4. Defines an interface for accessing a component's parent in the
       recursive structure, and implements it if that's appropriate.
    """
    def operation(self):
        raise NotImplementedError

    def add(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError

    def get_child(self):
        raise NotImplementedError


class Leaf(Component):
    """
    1. Represents leaf objects in the composition. A leaf has no children.
    2. Defines behavior for primitive objects in the composition.
    """
    def __init__(self, name):
        self.name = name

    def operation(self):
        print self.name


class Composite(Component):
    """
    1. Defines behavior for components having children.
    2. Stores child components.
    3. Implements child-related operations in the Component interface.
    """
    def __init__(self):
        self.children = list()

    def operation(self):
        for c in self.children:
            c.operation()

    def add(self, c):
        self.children.append(c)

    def remove(self):
        self.children.pop(c)

    def get_child(self, index):
        return self.children[index]


class Client(object):
    """
    Manipulates objects in the composition through the Component interface.
    """
    def main(self):
        # Clients use the Component class interface to interact with objects
        # in the composite structure. If the recipient is a Leaf, then the
        # request is handled directly. If the recipient is a Composite, then
        # it usually forwards requests to its children, possibly performing
        # additional operations before and/or after forwarding.
        root = Composite()
        n = 0
        for i in range(0,3):
            c = Composite()
            for j in range(0,4):
                leaf = Leaf(n)
                c.add(leaf)
                n += 1
            root.add(c)
        root.operation()


if __name__ == '__main__':
    c = Client()
    c.main()
