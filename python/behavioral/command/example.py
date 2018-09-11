import argparse
import logging
import unittest


class Command(object):
    def __init__(self, receiver):
        assert(isinstance(receiver, Receiver))
        logging.info('({}) Set command receiver'.format(type(self).__name__))
        self.receiver = receiver
        self.history = ['Foo','Bar','Baz']

    def execute(self):
        raise NotImplementedError


class SimpleCommand(Command):
    def execute(self, args):
        logging.info('({}) Call action() on receiver'.format(type(self).__name__))
        return self.receiver.action(args.name)


class ComplexCommand(Command):
    def execute(self, args):
        logging.info('({}) Call action() on receiver'.format(type(self).__name__))
        self.history.append(args.name)
        return self.receiver.action(args.name)
    def unexecute(self):
        logging.info('({}) Call undo() on receiver'.format(type(self).__name__))
        name = self.history.pop()
        return self.receiver.undo(name)


class Receiver(object):
    def action(self, name):
        logging.info('({}) Say hello'.format(type(self).__name__))
        return 'Hello, {}!'.format(name)
    def undo(self, name):
        logging.info('({}) Say goodbye'.format(type(self).__name__))
        return 'Goodbye, {}!'.format(name)


class DefaultReceiver(Receiver):
    def action(self, name):
        logging.info('({}) Default'.format(type(self).__name__))
        return 'Nothing to do ...'


class SimpleClient(object):
    def __init__(self, obj):
        assert(isinstance(obj.invoker, Invoker))
        logging.info('[SimpleClient] Create command')
        switcher = {
            'greet': Receiver()
        }
        receiver = switcher.get(obj.args.cmd, DefaultReceiver())
        command = SimpleCommand(receiver)
        obj.invoker.storeCommand(command)


class ComplexClient(object):
    def __init__(self, obj):
        assert(isinstance(obj.invoker, Invoker))
        logging.info('[ComplexClient] Create command')
        switcher = {
            'greet': Receiver(),
            'dismiss': Receiver()
        }
        receiver = switcher.get(obj.args.cmd, DefaultReceiver())
        command = ComplexCommand(receiver)
        obj.invoker.storeCommand(command)


class Invoker(object):
    def __init__(self):
        logging.info('({}) New Invoker'.format(type(self).__name__))
        self._command = None
    def storeCommand(self, command):
        assert(isinstance(command, Command))
        logging.info('({}) Store command'.format(type(self).__name__))
        self._command = command
    def operation1(self, args):
        logging.info('({}) Call execute() on command'.format(type(self).__name__))
        return self._command.execute(args)
    def operation2(self):
        logging.info('({}) Call unexecute() on command'.format(type(self).__name__))
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
        self.assertEquals(self.invoker.operation1(self.args), 'Hello, World!')
    def test_2(self):
        self.args.cmd = 'dismiss'
        ComplexClient(self)
        self.assertEquals(self.invoker.operation2(), 'Goodbye, Baz!')
        self.assertEquals(self.invoker.operation2(), 'Goodbye, Bar!')
        self.assertEquals(self.invoker.operation2(), 'Goodbye, Foo!')


if __name__ == '__main__':
    unittest.main()
