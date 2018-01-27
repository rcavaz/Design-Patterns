"""
PROXY

Use this pattern whenever there is a need of a more versatile or sophisticated
reference to an object than a simple pointer.
"""
class Subject(object):
    """
    Defines the common interface for RealSubject and Proxy so that Proxy can
    be used anywhere a RealSubject is expected.
    """
    def request(self):
        raise NotImplementedError


class RealSubject(Subject):
    """
    Defines the real object that the proxy represents.
    """
    def request(self):
        print 'Hello, World!'


class Proxy(Subject):
    """
    1. Maintains a reference that lets the proxy access the real subject.
       Proxy may refer to a Subject if the RealSubject and Subject interfaces
       are the same.
    2. Provides an interface identical to Subject's so that a proxy can be
       substituted for the real subject.
    3. Controls access to the RealSubject and may be responsible for creating
       and deleting it.
    """
    def __init__(self):
        self.real = RealSubject()

    def request(self):
        #...
        self.real.request()
        #...


class Client(object):
    def main(self):
        # Proxy forwars requests to RealSubject when appropriate, depending
        # on the kind of proxy.
        p = Proxy()
        p.request()
