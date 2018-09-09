import logging
import unittest


"""
Use the Singleton pattern when:
    - there must be exactly one instance of a class, and it must be accessible
      to clients from a well-known access point.
    - when the sole instance should be extensible by subclassing, and clients
      should be able to use an extended instance without modifying their code.
"""
class Singleton(object):
    """
    - Defines an Instance operation that lets clients access its unique
      instance. Instance is a class operation.
    - May be responsible for creating its own unique instance.
    """
    __shared_state = {}
    def __init__(self, name):
        if not Singleton.__shared_state:
            logging.basicConfig(level=logging.INFO)
            logging.info('New instance created!')
        else:
            logging.info('State reused!')
        self.__dict__ = self.__shared_state
        self.name = name


class TestSingletonPattern(unittest.TestCase):
    """
    - Clients access a Singleton instance solely through Singleton's Instance
      operation.
    """
    def setUp(self):
        self.a = Singleton('First')

    def test_1(self):
        self.assertEqual(self.a.name, 'First')

    def test_2(self):
        b = Singleton('Second')
        self.assertNotEqual(id(self.a), id(b))
        self.assertEqual(self.a.name, b.name)
        self.assertEqual(self.a.name, 'Second')

    def tearDown(self):
        self.a = None


"""
Consequences

    1. Controlled access to sole instance. Because the Singleton class
       encapsulates its sole instance, it can have strict control over how and
       when clients access it.

    2. Reduced name space. The Singleton pattern in an improvement over global
       variables. It avoids polluting the name space with global variables
       that store sole instances.

    3. Permits refinement of operations and representation. The Singleton
       class may be subclassed, and it's easy to configure an application with
       an instance of this extended class. You can configure the application\
       with an instance of the class you need at run-time.

    4. Permits a variable number of instances. The pattern makes it easy to
       change your mind and allow more than one instance of the Singleton
       class. Moreover, you can use the same approach to control the number of
       instances that the applications uses. Only the operation that grants
       access to the Singleton instance need to change.

    5. More flexible than class operations. Another way to package a
       singleton's functionality is to use class operations. But both of these
       language techniques make it hard to change a design to allow more than
       one instance of a class.
"""

if __name__ == '__main__':
    unittest.main()
