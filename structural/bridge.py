#!/usr/bin/env python
"""
BRIDGE (a.k.a. Handle/Body)

Use this pattern when:
    1. you want to avoid permanent binding between an abstraction and its
       implementation.
    2. both the abstractions and their implementations should be extensible by
       subclassing. In this case, the Bridge pattern lets you combine the
       different abstractions and implementations and extend them
       independently.
    3. changes in the implementation of an abstraction should have no impact
       on clients; that is, their code should not have to be recompiled.
    4. you have a proliferation of classes. This indicates the need for
       splitting an object into two parts (nested generalizations).

"""
class Implementor:
    """
    Defines the interface for implementation classes. This interface doesn't
    have to correspond exactly to Abstraction's interface; in fact, they could
    be quite different. Typically the Implementor interface provides only
    primitive operations, and Abstraction defines higher-level operations
    based on these primitives.
    """
    def implemented_operation(self):
        raise NotImplementedError


class ConcreteImplementorA(Implementor):
    """
    Implements the Implementor interface and defines its concrete
    implementation.
    """
    def implemented_operation(self):
        pass


class ConcreteImplementorB(Implementor):
    def implemented_operation(self):
        pass


class Abstraction:
    """
    Defines the abstraction's interface and
    Maintains a reference to an object of type Implementor.
    """
    def operation(self):
        raise NotImplementedError


class RefinedAbstraction(Abstraction):
    """
    Extends the interface defined by Abstraction.
    """
    imp = ConcreteImplementorA()
    #imp = ConcreteImplementorB()
    def operation(self):
        self.imp.implemented_operation()


class Client:
    """
    Requests operation to Refined Abstraction.
    """
    def main(self):
        a = RefinedAbstraction()
        a.operation()


if __name__ == '__main__':
    c = Client()
    c.main()
