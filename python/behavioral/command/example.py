import argparse
import logging


class Command(object):
    def __init__(self, receiver):
        assert(isinstance(receiver, Receiver))
        logging.info('({}) Set command receiver'.format(type(self).__name__))
        self.receiver = receiver
        self.state = None

    def execute(self):
        raise NotImplementedError


class ConcreteCommand(Command):
    def execute(self, args):
        logging.info('({}) Call action() on receiver'.format(type(self).__name__))
        return self.receiver.action(args.name)


class Receiver(object):
    def action(self, name):
        logging.info('({}) Say hello'.format(type(self).__name__))
        return 'Hello, {}!'.format(name)


class DefaultReceiver(Receiver):
    def action(self, name):
        logging.info('({}) Say hello'.format(type(self).__name__))
        return 'Nothing to do ...'


class Client(object):
    def __init__(self, invoker, cmd):
        assert(isinstance(invoker, Invoker))
        logging.info('({}) Create command'.format(type(self).__name__))
        if cmd == 'greet':
            receiver = Receiver()
        else:
            receiver = DefaultReceiver()
        command = ConcreteCommand(receiver)
        invoker.storeCommand(command)


class Invoker(object):
    def __init__(self):
        logging.info('({}) New Invoker'.format(type(self).__name__))
        self._command = None
    def storeCommand(self, command):
        assert(isinstance(command, Command))
        logging.info('({}) Store command'.format(type(self).__name__))
        self._command = command
    def operation(self, args):
        logging.info('({}) Call execute() on command'.format(type(self).__name__))
        return self._command.execute(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', help='Command to run', type=str)
    parser.add_argument('name', help='Who to greet', type=str)
    parser.add_argument('-v', '--verbosity', action='store_true', help='increase output verbosity')
    args = parser.parse_args()

    if args.verbosity:
        logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    else:
        logging.basicConfig(level=logging.WARNING, format='[%(levelname)s] %(message)s')


    def client(invoker):
        Client(invoker, 'greet')
    def default(invoker):
        Client(invoker, 'default')

    switcher = {
        'greet': client
    }
    func = switcher.get(args.cmd, default)
    invoker = Invoker()
    func(invoker)
    print(invoker.operation(args))
