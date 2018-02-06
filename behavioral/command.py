#!/usr/bin/env python
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
class Command(object):
    """
    Declares an interface for executing an operation.
    """
    def __init__(self, receiver):
        self.receiver = receiver
        self.state = None

    def execute(self):
        raise NotImplementedError


class ConcreteCommand(Command):
    """
    1. Defines a binding between a Receiver object and an action.
    2. Implements Execute by invoking the corresponding operation(s) on
       Receiver.
    """
    def execute(self):
        self.receiver.action()


class Receiver(object):
    """
    Knows how to perform the operations associated with carrying out a request.
    Any class may serve as a Receiver.
    """
    def action(self):
        print 'Hello, World!'


class Client(object):
    """
    Creates a ConcreteCommand object and sets its receiver.
    """
    def __init__(self, invoker):
        command = ConcreteCommand(Receiver())
        invoker.storeCommand(command)


class Invoker(object):
    """
    Asks the command to carry out the request.
    """
    def __init__(self):
        self._command = None

    def storeCommand(self, command):
        self._command = command

    def operation(self):
        self._command.execute()


if __name__ == '__main__':
    # 1. The client creates a ConcreteCommand object and specifies its receiver.
    # 2. An Invoker object stores the ConcreteCommand object.
    i = Invoker()
    c = Client(i)
    # 3. The invoker issues a request by calling execute() on the command.
    #    When commands are undoable, ConcreteCommand stores state for undoing
    #    the command prior to invoking execute().
    # 4. The ConcreteCommand object invokes operations on its reciver to
    #    carryout the request.
    i.operation()
