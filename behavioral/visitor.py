#!/usr/bin/env
class Visitor(object):
    """
    Declares a Visit operation for each class of ConcreteElement in the object structure.
    The operation's name and signature identifies the class that sends the Visit request to the visitor.
    That lets the visitor determine the concrete class of the element being visited.
    Then the visitor can access the element directly through its particular interface.
    """
    def visitConcreteElementA(self, element):
        raise NotImplementedError

    def visitConcreteElementB(self, element):
        raise NotImplementedError


class ConcreteVisitor1(Visitor):
    """
    Implements each operation declared by Visitor.
    Each operation implements a fragment of the traverse defined for the corresponding class of object in the structure.
    ConcreteVisitor provides the context for the traverse and stores its local state.
    This state often accumulates results during the traversal of the structure.
    """
    def visitConcreteElementA(self, element):
        print 'Hello, %s' % element.name

    def visitConcreteElementB(self, element):
        print 'Wassup, %s' % element.name


class ConcreteVisitor2(Visitor):
    def visitConcreteElementA(self, element):
        print 'Delete %s' % element.name

    def visitConcreteElementB(self, element):
        print 'Destroy %s' % element.name


class Element(object):
    """
    Defines an Accept operation that takes a visitor as an argument.
    """
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        raise NotImplementedError


class ConcreteElementA(Element):
    """
    Implements an Accept operation that takes a visitor as an argument.
    """
    def accept(self, visitor):
        visitor.visitConcreteElementA(self)

    def operationA(self):
        pass


class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visitConcreteElementB(self)

    def operationB(self):
        pass

class ObjectStructure(object):
    """
    Can enumerate its elements.
    May provide a high-level interface to allow the visitor to visit its elements.
    May either be a composite (see Composite(183)) or a collection such as a list or a set.
    """
    def __init__(self, e, v=None):
        self.elements = e
        self.visitor  = v

    def setVisitor(self, v):
        self.visitor = v

    def traverse(self):
        v = self.visitor
        for e in self.elements:
            e.accept(v)


class Client(object):
    """
    A client that uses the Visitor pattern must create a ConcreteVisitor object and then traverse the object structure, visiting each element with the visitor.
    When an element is visited, it calls the Visitor operation that corresponds to its class.
    The element supplies itself as an argument to this operation to let the visitor access its state, if necessary.
    """
    def main(self):
        # Initialize object structure
        elements = []
        elements.append( ConcreteElementA('A') )
        elements.append( ConcreteElementA('B') )
        elements.append( ConcreteElementB('C') )
        obj = ObjectStructure(elements)

        # Traverse with visitor 1
        visitor  = ConcreteVisitor1()
        obj.setVisitor(visitor)
        obj.traverse()

        # Traverse with visitor 2
        visitor  = ConcreteVisitor2()
        obj.setVisitor(visitor)
        obj.traverse()


if __name__ == '__main__':
    c = Client()
    c.main()
