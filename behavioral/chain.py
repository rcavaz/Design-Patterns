#!/usr/bin/env python
"""
CHAIN OF RESPONSIBILITY

Use this pattern when:
    1. more than one object can handle a request, and the handler isn't known
       apriori.
    2. you want to issue a request to one of several objects without
       specifying the receiver explicitly.
    3. the set of objects that can handle a request should be specified
       dynamically.
"""
class Handler(object):
    """
    1. Defines an interface for handling requests.
    2. Optionally implements the successor link.
    """
    def __init__(self, successor=None):
        self._successor = successor

    def __str__(self):
        return 'Handler'

    def handle_request(self):
        raise NotImplementedError


class ConcreteHandler1(Handler):
    """
    1. Handles requests it is responsible for.
    2. Can access its successor.
    3. if the ConcreteHandler can handle the request, it does so;
       otherwise it forwards the request to its successor.
    """
    def handle_request(self, handle=False):
        if handle:
            print 'Request handled by: %s' % type(self)
        elif self._successor is not None:
            self._successor.handle_request()
        else:
            print 'Could not handle request'


class ConcreteHandler2(Handler):
    def handle_request(self, handle=False):
        if handle:
            print 'Request handled by: %s' % type(self)
        elif self._successor is not None:
            self._successor.handle_request()


class Client(object):
    def main(self):
        h1 = ConcreteHandler1()
        h1.handle_request(True)

        h2 = ConcreteHandler2(h1)
        h2.handle_request(True)
        h2.handle_request(False)


if __name__ == '__main__':
    c = Client()
    c.main()
