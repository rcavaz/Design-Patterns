from abc import ABC, abstractmethod
import logging
import os
import unittest

"""
COMMAND (a.k.a. Action/Transaction)

Use this pattern when you want to:
    1. parameterize objects by an action to perform. You can express such
       parameterization in a procedural language with a callback function,
       that is, a function that's registetered somewhere to be called at a
       later point. Commands are an object-related replacement for callbacks.
    2. specify, queue, and execute requests at different times. A command
       object can have a lifetime independent of the original request. If the
       receiver of a request can be represented in an address space-independent
       way, then you can transfer a command object for the request to a
       different process and fulfill the request there.
    3. support undo. The Command's Execute operation can store state for
       reversing its effects in the command itself. The Command interface must
       have an added Unexecute operation that reverses the effects of a
       previous call to Execute.
       Executed commands are stored in a history list. Unlimited-level undo and
       redo is achieved by traversing this list backwards and forwards calling
       Unexecute and Execute, respectively.
    4. support logging changes so that they can be reapplied in case of a
       system crash. By audmenting the Command interface with load and store
       operations, you can keep a persistent log of changes. Recovering from
       a crash involves reloading logged commands from disk and reexecuting
       them with the Execute operation.
    5. structure a system around high-level operations built on primitives
       operations. Such a structure is common in information systems that
       support transactions. A transaction encapsulates a set of changes to
       data. The Command pattern offers a way to model transactions. Commands
       have a common interface, letting you invoke all transactions the same
       way. The pattern also makes it easy to extend the system with new
       transactions.
"""
class Receiver(object):
    """
    - Knows how to perform the operations associated with carrying out a request.
    - Any class may serve as a Receiver.
    """
    def action(self):
        logging.info(f'({type(self).__name__}) action()')
        return 'Hello, World!'


class Command(ABC):
    """
    - Declares an interface for executing an operation.
    """
    def __init__(self, receiver):
        logging.debug(f'New {self}')
        assert(isinstance(receiver, Receiver))
        logging.info(f'({self}) Set command receiver')
        self.receiver = receiver
        self.state = None

    def __str__(self):
        return type(self).__name__

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    """
    - Defines a binding between a Receiver object and an action.
    - Implements execute() by invoking the corresponding operation(s) on Receiver.
    """
    def execute(self):
        logging.info(f'({self}) execute()')
        return self.receiver.action()


class Invoker(object):
    """
    - Asks the command to carry out the request.
    """
    def __init__(self):
        logging.debug(f'New {self}')
        self._command = None

    def __str__(self):
        return type(self).__name__

    def store_command(self, command):
        assert(isinstance(command, Command))
        logging.info(f'({self}) store_command()')
        self._command = command

    def operation(self):
        logging.info(f'({self}) operation()')
        return self._command.execute()


class Client(object):
    """
    - Creates a ConcreteCommand object and sets its receiver.
    """
    def __init__(self, invoker):
        assert(isinstance(invoker, Invoker))
        logging.debug(f'New {type(self).__name__}')
        command = ConcreteCommand(Receiver())
        invoker.store_command(command)


class TestCommand(unittest.TestCase):
    def test_1(self):
        invoker = Invoker()
        Client(invoker)
        self.assertEqual(invoker.operation(), 'Hello, World!')


if __name__ == '__main__':
    loglevel = 'CRITICAL'
    for lvl in ['ERROR', 'WARNING', 'INFO', 'DEBUG']:
        if os.environ.get(lvl):
            loglevel = lvl
    levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    logging.basicConfig(
        level=levels.get(loglevel),
        format='[%(levelname)s] %(message)s')
    unittest.main()
