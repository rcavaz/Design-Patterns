#!/usr/bin/env python
"""
DECORATOR

Use this pattern:
    1. to add responsibiities to individual objects dynamically and
       transparently, that is, without affecting other objects.
    2. for responsibilities that can be withdrawn.
    3. when extension by subclassing is impractical. Sometimes a large number
       of independent extensions are possible and would produce an explosion
       of subclasses to support every combination. Or a class definition may
       be hidden or otherwise unavailable for subclassing.
"""
class Component(object):
    """
    Defines the interface for objects that can have responsibilities added
    to them dynamically.
    """
    def operation(self):
        raise NotImplementedError


class ConcreteComponent(Component):
    """
    Defines an object to which additional responsibilities can be attached.
    """
    def operation(self):
        print 'Hello, World!'


class Decorator(Component):
    """
    Maintains a reference to a Component object and defines an interface that
    conforms to Component's interface.
    """
    def operation(self, c):
        c.operation()


class ConcreteDecorator(Decorator):
    """
    Adds responsibilities to the component.
    """
    def __init__(self, state=None):
        self.addedState = state

    def operation(self, c):
        print '*** Ligths on! ***'
        super(ConcreteDecorator, self).operation(c)
        self.addedBehavior()

    def addedBehavior(self):
        print '*** Drops the mic ***'


class Client(object):
    def main(self):
        # Decorator forwards requests to its Component object. It may
        # optionally perform additional operations before and after forwarding
        # the request.
        c = ConcreteComponent()
        d = ConcreteDecorator()
        d.operation(c)


def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(txt):
            return "<%s>%s</%s>" % (tag_name, func(txt), tag_name)
        return func_wrapper
    return tags_decorator

@tags("p")
def welcome_msg(name):
    return 'Hello, '+name+'!'


if __name__ == '__main__':
    c = Client()
    c.main()
    print '----'
    print welcome_msg('World')
