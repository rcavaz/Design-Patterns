import logging
import unittest


class Visitor(object):
    def __init__(self):
        self.filtered = list()
    def visitConcreteElementA(self, element):
        assert(isinstance(element, ConcreteElementA))
        raise NotImplementedError

    def visitConcreteElementB(self, element):
        assert(isinstance(element, ConcreteElementB))
        raise NotImplementedError
    def result(self):
        return self.filtered


class NumericFilter(Visitor):
    def visitNumericElement(self, element):
        assert(isinstance(element, NumericElement))
        logging.info('({}) visiting NumberElement'.format(type(self).__name__))
        self.filtered.append(element)
    def visitCharElement(self, element):
        assert(isinstance(element, CharElement))
        logging.info('({}) visiting CharElement'.format(type(self).__name__))
        pass


class CharFilter(Visitor):
    def visitNumericElement(self, element):
        assert(isinstance(element, NumericElement))
        logging.info('({}) visiting NumberElement'.format(type(self).__name__))
        pass
    def visitCharElement(self, element):
        assert(isinstance(element, CharElement))
        logging.info('({}) visiting CharElement'.format(type(self).__name__))
        self.filtered.append(element)


class Element(object):
    def accept(self, visitor):
        raise NotImplementedError


class NumericElement(Element):
    def accept(self, visitor):
        assert(isinstance(visitor, Visitor))
        visitor.visitNumericElement(self)


class CharElement(Element):
    def accept(self, visitor):
        assert(isinstance(visitor, Visitor))
        visitor.visitCharElement(self)


class ObjectStructure(object):
    def __init__(self):
        self.elements = list()
        self.visitor = None
    def addElement(self, e):
        assert(isinstance(e, Element))
        self.elements.append(e)
    def setVisitor(self, v):
        assert(isinstance(v, Visitor))
        self.visitor = v
    def filter(self):
        for element in self.elements:
            element.accept(self.visitor)
        return self.visitor.result()


class TestVisitorPattern(unittest.TestCase):
    def setUp(self):
        self.obj = ObjectStructure()
        self.obj.addElement(NumericElement())
        self.obj.addElement(CharElement())
        self.obj.addElement(NumericElement())
        self.obj.addElement(NumericElement())
        self.obj.addElement(CharElement())
        self.obj.addElement(CharElement())
        self.obj.addElement(NumericElement())
        self.obj.addElement(CharElement())
    def test_1(self):
        self.obj.setVisitor(NumericFilter())
        result = self.obj.filter()
        for element in result:
            self.assertIsInstance(element, NumericElement)
    def test_2(self):
        self.obj.setVisitor(CharFilter())
        result = self.obj.filter()
        for element in result:
            self.assertIsInstance(element, CharElement)


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s %(message)s', level=logging.INFO)
    unittest.main()
