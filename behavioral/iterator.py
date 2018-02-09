"""
ITERATOR

Use the iterator pattern:
    1. to access an aggregate object's contents without exposing internal
       representation.
    2. to support multiple traversals of aggregate objects.
    3. to provide a uniform interface for traversing different aggregate
       structures.
"""
class Iterator(object):
    """
    Defines an interface for accessing and traversing elements.
    """
    def first(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def isDone(self):
        raise NotImplementedError

    def currentItem(self):
        raise NotImplementedError


class ConcreteIterator(Iterator):
    """
    1. Implements the Iterator interface.
    2. Keeps track of the current position in the traversal of the aggregate.
    """
    def __init__(self, obj):
        self.aggregate = obj

    def first(self):
        pass

    def next(self):
        pass

    def isDone(self):
        pass

    def currentItem(self):
        pass


class Aggregate(object):
    """
    Defines an interface for creating an Iterator object.
    """
    def createIterator(self):
        raise NotImplementedError


class ConcreteAggregate(Aggregate):
    """
    Implements the Iterator creation interface to return an instance of the
    proper ConcreteIterator.
    """
    def createIterator(self):
        return ConcreteIterator(self)


class Client(object):
    def main(self):
        obj = ConcreteAggregate()
        i = obj.createIterator()
        i.first()
        i.next()
        i.currentItem()
        i.isDone()


if __name__ == '__main__':
    c = Client()
    c.main()
