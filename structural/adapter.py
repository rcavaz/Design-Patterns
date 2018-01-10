#!/usr/bin/env python
"""
ADAPTER (a.k.a. Wrapper)

Use this pattern when:
    1. you want to use an existing class, and its interface does not match the
       one you need.
    2. you want to create a reusable class that cooperates with unrelated or
       unforseen classes, that is, classes that don't necessarily have
       compatible interfaces.
    3. (object adapter only) you need to use several existing subclasses,
       but it's impractical to adapt their interface by subclassing every one.
       An object adapter can adapt the interface of its parent class.


Implementation

    Suppose that we have the classes: a) Runner, b) Sprinter and c) Walker;
    with properties run, sprint and walk respectively. Know suppose we want
    to reuse them but as you will see they don't have a common interface.

    We will create a Target interface called Person for our Client to use
    and an Adapter that will adapt our Runner, Sprinter and Walker classes
    into the Target interface (Person).
"""
class Person(object):
    """
    Target
    Defines the domain-specific interface that Client uses.
    """
    def action(self):
        raise NotImplementedError


class Runner(object):
    """
    Adaptee
    Defines an existing interface that needs adapting.
    """
    def __str__(self):
        return 'Runner'

    def run(self):
        return '%s runs at a rate of 15 mph on average.' % self


class Sprinter(object):
    """
    Adaptee
    """
    def __str__(self):
        return 'Sprinter'

    def sprint(self):
        return '%s runs at a top speed of 27 mph.' % self


class RunnerClassAdapter(Person, Runner):
    """
    Adapter
    Adapts the interface of Adaptee to the Target interface.

    A class adapter uses multiple inheritance and has the following
    trade-offs:
        1. adapts Adaptee to Target by committing to a concrete Adapter class.
           As a consequence, it won't work when we want to adapt a class and
           all its sublcasses.
        2. lets Adapter override some of Adaptee's behavior, since Adapter is
           a subclass of Adaptee.
        3. introduces only one object, and no additional pointer indirection
           is needed to get to the adaptee.
    """
    def action(self):
        return self.run()


class SprinterClassAdapter(Person, Sprinter):
    """
    Adapter
    """
    def action(self):
        return self.sprint()


class ObjectAdapter(Person):
    """
    Adapter

    An object adapter relies on object composition and has the following
    trade-offs:
        1. lets a single Adapter work with many Adaptees, that is, the Adaptee
           itself and all of its subclasses (if any). The Adapter can add
           functionality to all Adaptees at once.
        2. makes it harder to override Adaptee behavior because it will
           require subclassing Adaptee and making Adapter refer to the
           subclass rathern than the Adaptee itself.
    """
    def __init__(self, obj):
        self.obj = obj

    def action(self):
        if str(self.obj) == 'Runner':
            return self.obj.run()

        elif str(self.obj) == 'Sprinter':
            return self.obj.sprint()

        elif str(self.obj) == 'Walker':
            return self.obj.walk()

        else:
            raise NotImplementedError


class PythonObjectAdapter(Person):
    """
    Adapter

    This implementation makes use of Python's built in functions and should
    be the prefered way for implementing this design pattern.

    Notice that this implementation does not require the class to inherit
    from Target, but not doing so may be misleading in some situations.
    """
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        # __dict__ is a special attribute that stores an object's (writable)
        # attributes as a dictionary or another mapping object.
        # Here we use it to map our adapter attribute with our adaptee
        # function attribute.
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        # You can tell a class how to deal with attributes it doesn't
        # explicitly manage via the __getattr__ method.
        # Here we tell it to return the attribute value of self.obj.attr
        # through the getattr() method, and attr will be the adaptee
        # function attribute thanks to __init__ setting __dict__.
        return getattr(self.obj, attr)


class Client(object):
    """
    Client
    Collaborates with objects conforming to the Target interface.
    """
    def main(self):
        # Clients call operations on an Adapter instance. In turn, the
        # adapter calls Adaptee operations that carry out the request.
        a = []

        print '-- Using Class Adapters --'
        for adapter in [RunnerClassAdapter, SprinterClassAdapter]:
            a.append(adapter())
        print a[0].action()
        print a[1].action()
        print ''

        print '-- Using Object Adapter --'
        for person in [Runner, Sprinter]:
            p = person()
            if str(p) == 'Runner':
                attr = p.run
            elif str(p) == 'Sprinter':
                attr = p.sprint
            elif str(p) == 'Walker':
                attr = p.walk
            else:
                raise NotImplementedError
            a.append(ObjectAdapter(p))
        print a[2].action()
        print a[3].action()
        print ''

        print '-- Using Python Object Adapter --'
        for person in [Runner, Sprinter]:
            p = person()
            if str(p) == 'Runner':
                attr = p.run
            elif str(p) == 'Sprinter':
                attr = p.sprint
            elif str(p) == 'Walker':
                attr = p.walk
            else:
                raise NotImplementedError
            a.append(PythonObjectAdapter(p, action=attr))
        print a[4].action()
        print a[5].action()
        print ''


if __name__ == '__main__':
    client = Client()
    client.main()
