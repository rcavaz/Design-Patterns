"""
MEDIATOR

Use the pattern when:
    1. a set of objects communicate in well-defined but complex ways.
       The resulting interdependencies are unstructured and difficult to
       understand.
    2. reusing an object is difficult because it refers to and communicates
       with many other objects.
    3. a behavior that's distributed between several classes should be
       customizable without a lot of subclassing.
"""
class Mediator(object):
    """
    Defines an interface for communicating with Colleague objects.
    """
    pass


class ConcreteMediator(Mediator):
    """
    1. Implements cooperative behavior by coordinating Colleague objects.
    2. Knows and maintains its colleagues.
    """
    pass


class Colleague(object):
    """
    1. Each Colleague class knows its Mediator object.
    2. Each Colleague communicates with its mediator whenever it would have
       otherwise communicated with another colleague.
    """
    pass


class ConcreteColleague1(Colleague):
    """
    Implements the Colleague interface.
    """
    pass


class ConcreteColleague2(Colleague):
    pass


class Client(object):
    def main(self):
        # Colleagues send and receive requests from a Mediator object.
        # The mediator implements the cooperative behavior by routing requests
        # between the appropriate colleagues.
        pass


if __name__ == '__main__':
    c = Client()
    c.main()
