#!/usr/bin/env python
"""
FACADE

Use this pattern when:
   1. you want to provide a simple interface to a complex subsystem. Subsystems often get more complex as they evolve. Most patterns, when applied, result in more and smaller classes. This makes the subsystem more reusable and easier to customize, but it also becomes harder to use for clients that don't need to customize it. A facade can provide a simple default view of the subsystem that is good enough for most clients. Only clients needing more customizability will need to look beyond the facade.
   2. there are many dependencies between clients and the implementation classes of an abstraction. Introduce a facade to decouple the subsystem from clients and other subsystems, thereby promoting subsystem independence and portability.
   3. you want to layer your subsystems. Use a facade to define an entry point to each subsystem level. If subsystems are dependent, then you can simplify the dependencies between them by making them communicate with each other solely through their facades.
"""
class SubsystemClassA(object):
    """
    1. implement subsystem functionality.
    2. handle work assigned by the Facade object.
    3. have no knowledge of the facade; that is, they keep no references to it.
    """
    def operation(self):
        print 'Hello, World!'


class SubsystemClassB(object):
    def operation(self):
        print 'Wassup, Bro!!'


class Facade(object):
    """
    1. knows which subsystem classes are responsible for a request.
    2. delegates client requests to appropriate subsystem objects.
    """
    def operationA(self):
        obj = SubsystemClassA()
        obj.operation()

    def operationB(self):
        obj = SubsystemClassB()
        obj.operation()


class Client(object):
    def main(self, cmd):
        # Clients communicate with the subsystem by sending requests to Facade,
        # which forwards them to the approrpiate subsystem object(s). Although
        # the subsystem objects perform the actual work, the facade may have
        # to do work of its own to translate its interface to subsystem
        # interfaces.
        #
        # Clients that use the facade don't have to access it's subsystem
        # objects directly.
        compiler = Facade()
        if cmd == 'hello':
            compiler.operationA()
        elif cmd == 'hi':
            compiler.operationB()
        else:
            raise NotImplementedError


if __name__ == '__main__':
    c = Client()
    c.main('hello')
    c.main('hi')
