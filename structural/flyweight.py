#!/usr/bin/env python
"""
FLYWEIGHT

Use this pattern when all the following are true:
    1. An application uses a large number of objects.
    2. Storage costs are high because of the sheer quantity of objects.
    3. Most object state can be made extrinsic.
    4. Many groups of objects may be replaced by relatively few shared objects once extrinsic state is removed.
    5. The application doesn't depend on object identity. Since flyweight objects may be shared, identity tests will return true for conceptually distinct objects.
"""
class Flyweight(object):
    def operation(self, extrinsicState):
        raise NotImplementedError


class ConcreteFlyweight(Flyweight):
    def __init__(self, state=None):
        self.intrinsicState = state

    def operation(self, extrinsicState):
        print '%s, %s!' % (extrinsicState, self.intrinsicState)


class UnsharedConcreteFlyweight(Flyweight):
    def __init__(self, state=None):
        self.allState = state

    def operation(self, extrinsicState):
        pass


class FlyweightFactory(object):
    def __init__(self):
        self.flyweights = dict()

    def getFlyweight(self, key):
        if key in self.flyweights:
            return self.flyweights[key]
        else:
            w = ConcreteFlyweight(key)
            self.flyweights[key] = w
            return w


class Client(object):
    def main(self):
        factory = FlyweightFactory()
        for i in ['A', 'B', 'C', 'A']:
            obj = factory.getFlyweight(i)
            obj.operation('Hello')


if __name__ == '__main__':
    c = Client()
    c.main()
