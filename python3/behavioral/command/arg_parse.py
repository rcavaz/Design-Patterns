from abc import ABC, abstractmethod
import argparse
import logging
import unittest


class Command(ABC):
    def __init__(self, receiver):
        assert(isinstance(receiver, Receiver))
        logging.info(f'({self}) Set command receiver')
        self.receiver = receiver
        self.history = ['Foo', 'Bar', 'Baz']

    def __str__(self):
        return type(self).__name__

    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):
    def execute(self, args):
        logging.info(f'({self}) Call action() on receiver')
        return self.receiver.action(args.name)


class ComplexCommand(Command):
    def execute(self, args):
        logging.info(f'({self}) Call action() on receiver')
        self.history.append(args.name)
        return self.receiver.action(args.name)

    def unexecute(self):
        logging.info(f'({self}) Call undo() on receiver')
        name = self.history.pop()
        return self.receiver.undo(name)


class Receiver:
    def __srt__(self):
        return type(self).__name__

    def action(self, name):
        logging.info(f'({self}) Say hello')
        return f'Hello, {name}!'

    def undo(self, name):
        logging.info(f'({self}) Say goodbye')
        return f'Goodbye, {name}!'



class SimpleClient(object):
    def __init__(self, obj):
        assert(isinstance(obj.invoker, Invoker))
        logging.info(f'({self}) Create command')
        switcher = {
            'greet': Receiver()
        }
        receiver = switcher.get(obj.args.cmd)
        command = SimpleCommand(receiver)
        obj.invoker.storeCommand(command)


class ComplexClient(object):
    def __init__(self, obj):
        assert(isinstance(obj.invoker, Invoker))
        logging.info(f'({self}) Create command')
        switcher = {
            'greet': Receiver(),
            'dismiss': Receiver()
        }
        receiver = switcher.get(obj.args.cmd)
        command = ComplexCommand(receiver)
        obj.invoker.storeCommand(command)


class Invoker(object):
    def __init__(self):
        logging.info(f'New {self}')
        self._command = None

    def __str__(self):
        return type(self).__name__

    def storeCommand(self, command):
        assert(isinstance(command, Command))
        logging.info(f'({self}) Store command')
        self._command = command

    def operation1(self, args):
        logging.info(f'({self}) Call execute() on command')
        return self._command.execute(args)

    def operation2(self):
        logging.info(f'({self}) Call unexecute() on command')
        return self._command.unexecute()


class Namespace(object):
    pass


class TestCommandPattern(unittest.TestCase):
    def setUp(self):
        # parser = argparse.ArgumentParser()
        # parser.add_argument('-v', '--verbosity', action='store_true', help='increase output verbosity')
        # parser.add_argument('cmd', help="Choose from 'greet' or 'dismiss'", type=str)
        # parser.add_argument('--name', help='Who to greet', type=str, default='World')
        # args = parser.parse_args()
        self.args = Namespace()
        #
        # if args.verbosity:
        #     logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
        # else:
        #     logging.basicConfig(level=logging.WARNING, format='[%(levelname)s] %(message)s')
        #
        self.invoker = Invoker()

    def test_1(self):
        # Namespace.cmd = property(lambda self: 'greet')
        # Namespace.name = property(lambda self: 'World')
        self.args.cmd = 'greet'
        self.args.name = 'World'
        SimpleClient(self)
        self.assertEqual(self.invoker.operation1(self.args), 'Hello, World!')

    def test_2(self):
        self.args.cmd = 'dismiss'
        ComplexClient(self)
        self.assertEqual(self.invoker.operation2(), 'Goodbye, Baz!')
        self.assertEqual(self.invoker.operation2(), 'Goodbye, Bar!')
        self.assertEqual(self.invoker.operation2(), 'Goodbye, Foo!')


if __name__ == '__main__':
    unittest.main()
