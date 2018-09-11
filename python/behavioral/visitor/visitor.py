import logging
import unittest


"""
Use the Visitor pattern when:
    - an object structure contains many classes of objects with differing
      interfaces, and you want to perform operations on these objects that
      depend on their concrete classes.
    - many distinct and unrelated operations need to be performed on objects
      in an object structure, and you want to avoid "polluting" their classes
      with these operations. Visitor lets you keep related operations together
      by defining them in one class. When the object structure is shared by
      many applications, use Visitor to put operations in just those
      applications that need them.
    - the classes defining the object structure rarely change, but you often
      want to define new operations over the structure. Changing the object
      structure classes requires redefining the interface to all visitors,
      which is potentially costly. If the object structure classes change
      often, then it's probably better to define the operations in those
      classes.
"""
class Visitor(object):
    """
    - Declares a 'Visit' operation for each class of ConcreteElement in the
      object structure. The operation's name and signature identifies the
      class that sends the Visit request to the visitor. That lets the visitor
      determine the concrete class of the element being visited. Then the
      visitor can access the element directly through its particular interface.
    """
    def visitConcreteElementA(self, element):
        assert(isinstance(element, ConcreteElementA))
        raise NotImplementedError

    def visitConcreteElementB(self, element):
        assert(isinstance(element, ConcreteElementB))
        raise NotImplementedError


class ConcreteVisitor1(Visitor):
    """
    - Implements each operation declared by Visitor. Each operation implements
      a fragment of the algorithm defined for the corresponding class of
      object in the structure. ConcreteVisitor provides the context for the
      algorithm and stores its local state. This state often accumulates
      results during the traversal of the structure.
    """
    def visitConcreteElementA(self, element):
        assert(isinstance(element, ConcreteElementA))
        logging.info('Visitor1 - ElementA')
    def visitConcreteElementB(self, element):
        assert(isinstance(element, ConcreteElementB))
        logging.info('Visitor1 - ElementB')


class ConcreteVisitor2(Visitor):
    def visitConcreteElementA(self, element):
        assert(isinstance(element, ConcreteElementA))
        logging.info('Visitor2 - ElementA')
    def visitConcreteElementB(self, element):
        assert(isinstance(element, ConcreteElementB))
        logging.info('Visitor2 - ElementB')


class Element(object):
    """
    - Defines an 'Accept' operation that takes a visitor as an argument.
    """
    def accept(self, visitor):
        raise NotImplementedError


class ConcreteElementA(Element):
    """
    - Implements an 'Accept' operation that takes visitor as an argument.
    """
    def accept(self, visitor):
        assert(isinstance(visitor, Visitor))
        visitor.visitConcreteElementA(self)


class ConcreteElementB(Element):
    def accept(self, visitor):
        assert(isinstance(visitor, Visitor))
        visitor.visitConcreteElementB(self)


class ObjectStructure(object):
    """
    - Can enumarte its elements.
    - May provide a high-level interface to allow the visitor to visit its
      elements.
    - May either be a composite or a collection such as a list or a set.
    """
    def __init__(self):
        self.elements = list()
        self.visitor = None
    def addElement(self, e):
        assert(isinstance(e, Element))
        self.elements.append(e)
    def setVisitor(self, v):
        assert(isinstance(v, Visitor))
        self.visitor = v
    def traverse(self):
        for element in self.elements:
            element.accept(self.visitor)


class TestVisitorPattern(unittest.TestCase):
    """
    - A client that uses the Visitor pattern must create a ConcreteVisitor
      object and then traverse the object structure, visiting each element
      with the visitor.
    - When an element is visited, it calls the Visitor operation that
      corresponds to its class. The element supplies itself as an argument to
      this operation to let the visitor access its state, if necessary.
    """
    def setUp(self):
        self.obj = ObjectStructure()
        self.obj.addElement(ConcreteElementA())
        self.obj.addElement(ConcreteElementB())
    def test_1(self):
        self.obj.setVisitor(ConcreteVisitor1())
        self.obj.traverse()
    def test_2(self):
        self.obj.setVisitor(ConcreteVisitor2())
        self.obj.traverse()


"""
Consecuences

    1. Visitor makes adding new operations easy. Visitors make it easy to add
       operations that depend on the components of complext objects. You can
       define a new operation over an object structure simply by adding a new
       visitor. In contrast, if you spread functionality over many classes,
       then you must change each class to define a new operation.

    2. A visitor gathers related operations and separates unrelated ones.
       Related behavior isn't spread over the classes defining the object
       structure; it's localized in a visitor. Unrelated sets of behavior are
       partitioned in their own visitor subclasses. That simplifies both the
       classes defining the elements and the algorithms defined in the
       visitors. Any algorithm-specific data structures can be hidden in the
       visitor.

    3. Adding new ConcreteElement classes is hard. The Visitor pattern makes
       it hard to add new subclasses of Element. Each new ConcreteElement
       gives rise to a new abstract operation on Visitor and a corresponding
       implementation in every ConcreteVisitor class. Sometimes a default
       implementation can be provided in Visitor that can be inherited by
       most of the ConcreteVisitors, but this is the exception rather than the
       rule.

       So the key consideration in applying the Visitor pattern is whether you
       are mostly likely to change the algorithm applied over an object
       structure or the classes of the object that make up the structure. The
       Visitor class hierachy can be difficult to maintain when new
       ConcreteElement classes are added frequently. In such cases, it's
       probably easier just to define operations on the classes that make up
       the structure. If the Element class hierarchy is stable, but you are
       continually adding operations or changing algorithms, then the Visitor
       pattern will help you manage the changes.

    4. Visiting across class hierarchies. An iterator can visit the objects in
       a structure as it traverses them by calling their operations. But an
       iterator can't work across object structures with different types of
       elements.

    5. Accumulating state. Visitors can accumulate state as they visit each
       element in the object structure. Without a visitor, this state would be
       passed as extra arguments to the operations that perform the traversal,
       or they might appear as global variables.

    6. Breaking encapsulation. Visitor's approach assumes that the
       ConcreteElement interface is powerful enough to let visitors do their
       job. As a result, the pattern often forces you to provide public
       operations that access an element's internal state, which may
       compromise its encapsulation.
"""

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
