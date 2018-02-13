"""
OBSERVER

Use this pattern in any of these situations:
    1. When an abstraction has two aspects, one dependent on the other.
       Encapsulating these aspects in separate objects lets you vary andreuse
       them independently.
    2. When a change to one object requires changing others, and you don't
       know how many objects need to be changed.
    3. When an object should be able to notify other objects without making
       assumptions about who these objects are. In other words, you don't
       want these objects tightly coupled.
"""
class Subject(object):
    """
    1. Knows its observers. Any number of Observer may observe a subject.
    2. Provides an interface for attaching and detaching Observer objects.
    """
    def __init__(self):
        self.observers = dict()

    def attach(self, **observers):
        for observer in observers:
            self.observers[observer] = observers[observer]

    def detach(self, observer):
        self.observers.pop(observer, None)

    def notify(self):
        for o in self.observers:
            print 'Notifying: ' + o
            self.observers[o].update()


class Observer(object):
    """
    Defines an updating interface for objects that should be notified of
    changes in a subject.
    """
    def update(self):
        raise NotImplementedError


class ConcreteSubject(Subject):
    """
    1. Stores state of interest to ConcreteObserver objects.
    2. Sends a notification to its observers when its state changes.
    """
    def __init__(self):
        super(ConcreteSubject, self).__init__()
        self.subjectState = ''

    def getState(self):
        return self.subjectState

    def setState(self, state):
        self.subjectState = state
        self.notify()


class ConcreteObserver(Observer):
    """
    1. Maintains a reference to a ConcreteSubject object.
    2. Stores state that should stay consistent with the subject's.
    3. Implements the Observer updating interface to keep its state consistent
       with the subject's.
    """
    def __init__(self, subject):
        self.subject = subject
        self.observerState = 'x'

    def update(self):
        self.observerState = self.subject.getState()
        print 'State updated to: ' + self.observerState


class Client(object):
    def main(self):
        s1 = ConcreteSubject()
        o1 = ConcreteObserver(s1)
        o2 = ConcreteObserver(s1)
        s1.attach(a=o1, b=o2)
        s1.setState('Hello, World!')


if __name__ == '__main__':
    c = Client()
    c.main()
