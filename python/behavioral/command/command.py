import logging
import unittest


"""
Use this pattern when you want to:
    - parameterize objects by an action to perform. You can express such
      parameterization in a procedural language with a callback function,
      that is, a function that's registetered somewhere to be called at a
      later point. Commands are an object-related replacement for callbacks.

    - specify, queue, and execute requests at different times. A command
      object can have a lifetime independent of the original request. If the
      receiver of a request can be represented in an address space-independent
      way, then you can transfer a command object for the request to a
      different process and fulfill the request there.

    - support undo. The Command's Execute operation can store state for
      reversing its effects in the command itself. The Command interface must
      have an added Unexecute operation that reverses the effects of a
      previous call to Execute.
      Executed commands are stored in a history list. Unlimited-level undo and
      redo is achieved by traversing this list backwards and forwards calling
      Unexecute and Execute, respectively.

    - support logging changes so that they can be reapplied in case of a
      system crash. By audmenting the Command interface with load and store
      operations, you can keep a persistent log of changes. Recovering from
      a crash involves reloading logged commands from disk and reexecuting
      them with the Execute operation.

    - structure a system around high-level operations built on primitives
      operations. Such a structure is common in information systems that
      support transactions. A transaction encapsulates a set of changes to
      data. The Command pattern offers a way to model transactions. Commands
      have a common interface, letting you invoke all transactions the same
      way. The pattern also makes it easy to extend the system with new
      transactions.
"""
class Command(object):
    """
    - Declares an interface for executing an operation.
    """
    def __init__(self, receiver):
        assert(isinstance(receiver, Receiver))
        logging.info('[Command] Set command receiver')
        self.receiver = receiver
        self.state = None

    def execute(self):
        raise NotImplementedError


class ConcreteCommand(Command):
    """
    - Defines a binding between a Receiver object and an action.
    - Implements Execute by invoking the corresponding operation(s) on
      Receiver.
    """
    def execute(self):
        logging.info('[ConcreteCommand] Call action() on receiver')
        return self.receiver.action()


class Receiver(object):
    """
    - Knows how to perform the operations associated with carrying out a
      request. Any class may serve as a Receiver.
    """
    def action(self):
        logging.info('[Receiver] Greet the world')
        return 'Hello, World!'


class Client(object):
    """
    - Creates a ConcreteCommand object and sets its receiver.
    """
    def __init__(self, invoker):
        assert(isinstance(invoker, Invoker))
        logging.info('[Client] Create command')
        command = ConcreteCommand(Receiver())
        invoker.storeCommand(command)


class Invoker(object):
    """
    - Asks the command to carry out the request.
    """
    def __init__(self):
        logging.info('[Invoker] New Invoker')
        self._command = None

    def storeCommand(self, command):
        assert(isinstance(command, Command))
        logging.info('[Invoker] Store command')
        self._command = command

    def operation(self):
        logging.info('[Invoker] Call execute() on command')
        return self._command.execute()


class TestCommandPattern(unittest.TestCase):
    """
    Collaborations:
    """
    def setUp(self):
        self.invoker = Invoker()
    def test_1(self):
        """
        1. The client creates a ConcreteCommand object and aspecifies its receiver.
        2. An Invoker object stores the ConcreteCommand object.
        """
        Client(self.invoker)
        """
        3. The invoker issues a request by calling execute() on the command.
           When commands are undoable, ConcreteCommand stores state for undoing
           the command prior to invoking execute().
        4. The ConcreteCommand object invokes opoerations on its receiver to carry
           out the request.
        """
        self.assertEquals(self.invoker.operation(), 'Hello, World!')


"""
Consequences:

    1. Command decouples the object that invokes the operation from the one
       that knows how to perform it.
    2. Commands are first class objects. They can be manipulated and extended
       like any other object.
    3. You can assemble commands into a composite command. Composite commands
       are an instance of the Composite pattern.
    4. It's easy to add new Commands, because you don't have to change
       existing classes.
"""
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
