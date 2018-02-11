"""
STATE

Use this pattern when:
    1. Many related classes differ only in their behavior. Strategies provide
       a way to configure a class with one of many behaviors.
    2. You need different variants of an algorithm. For example, you might
       define algorithms reflecting space/time trade-offs. Strategies can be
       used when these variants are implemented as class hierarchy of
       algorithms.
    3. An algorithm uses data that clients shouldn't know about. Use the
       Strategy pattern to avoid exposing complex, algorithmic-specific
       datastructures.
    4. A class defines many behaviors, and these appear as multiple conditional
       statements in its operations. Instead of many conditionals, move related
       conditional branches into their own strategy class.
"""
class Strategy(object):
    """
    Declares an interface common to all supported algorithms. Context uses this
    interface to call the algorithm defined by a ConcreteStrategy.
    """
    def algorithm(self):
        raise NotImplementedError


class ConcreteStrategy(Strategy):
    """
    Implements the algorithm using the Strategy interface.
    """
    def algorithm(self, **args):
        pass


class Context(object):
    """
    1. Is configured with a ConcreteStrategy object.
    2. Maintains a reference to a Strategy object.
    3. May define an interface that lets Strategy access its data.
    """
    def __init__(self, strategy):
        self.strategy = strategy

    def contextInterface(self):
        pass

    def operation(self):
        self.strategy.algorithm(context=self)


class Client(object):
    # 1. Strategy and Context interact to implement the chosen algorithm. A
    #    context may pass all data required by the algorithm to the strategy
    #    when the algorithm is called. Alternatively, the context can pass
    #    itself as an argument to Strategy operations. That lets the strategy
    #    access its data.
    # 2. A context forwards requests from its clients to its strategy. Clients
    #    usually create and pass a ConcreteStrategy object to the context;
    #    thereafter, clients interact with the context exclusively. There is
    #    often a family of ConcreteStrategy classes to choose from.
    def main(self):
        s = ConcreteStrategy()
        c = Context(s)
        c.operation()


if __name__ == '__main__':
    c = Client()
    c.main()
