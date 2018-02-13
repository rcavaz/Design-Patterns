"""
TEMPLATE METHOD

Use this pattern:

1. To implement the invariant parts of an algorithm once and leave it upto
   subclasses to implement the behavior that can vary.
2. When common behavior among subclasses should be factored and localized in
   a common class to avoid code duplication. This is a good example of
   "refactoring to generalize" where you first identify the differences in the
   existing code, separate the differences into new operations and finally
   replace the differing code with a template method that calls one of these
   new operations.
3. To control subclasses extensions. You can define a template method that
   calls "hook" operations at specific points, thereby permitting extensions
   only at those points.
"""
class AbstractClass(object):
    """
    1. Defines abstract primitive operations that concrete subclasses define
       to implement steps of an algorithm.
    2. Implements a template method defining the skeleton of an algorithm.
       The template method calls primitive operations as well as operations
       defined in the AbastractClass or those of other objects.
    """
    def templateMethod(self):
        self.primitiveOperation1()
        self.primitiveOperation2()
        self.primitiveOperationN()

    def primitiveOperation1(self):
        pass

    def primitiveOperation2(self):
        raise NotImplementedError

    def primitiveOperationN(self):
        raise NotImplementedError


class ConcreteClass(AbstractClass):
    """
    Relies on AbstractClass to implement the invariant steps of the algorithm.
    """
    def primitiveOperation2(self):
        pass

    def primitiveOperationN(self):
        pass


class Client(object):
    def main(self):
        obj = ConcreteClass()
        obj.templateMethod()


if __name__ == '__main__':
    c = Client()
    c.main()
