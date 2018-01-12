#!/usr/bin/env python
"""
ABSTRACT FACTORY (a.k.a. Kit)

Use the Abstract Factory pattern when:
    1. a system should be independent of how its products are created,
       composed and represented.
    2. a system should be configured with one of the multiple families of
       products.
    3. a family of related product objects is designed to be used together,
       and you need to enforce this constraint.
    4. you want to provide a class library of products, and you want to reveal
       just their interfaces, not their implementations.


Implementation:

    Lets say we a set of 4 Drink products that are grouped as follows:
        1. Beer (family)
            1.1 Heineken
            1.2 Sapporo

        2. Soda (family)
            2.1 Melon Soda
            2.2 Ramune

    We will create an Abstract Factory called DrinkFactory that will serve as
    an interface for our Abstract Products of class Drink.

    We will also create a Concrete Factory per family named after the product
    they will create: 1) BeerFactory, and 2) SodaFactory.

    Then we will create an Abstract Product class called Drink that will
    define the interface for all our Concrete Products.

    Following this we will create a Concrete Product class for each our four
    products implementing the Abstract Product interface.

    Finally, we will create a Client class from which we will only use the
    interfaces defined by the AbstractFactory and AbstractProduct classes.
"""
import random


class DrinkFactory(object):
    """
    Abstract Factory
    Declares an interface for operations that create abstract product objects.

    It's up to ConcreteProduct subclasses to actually create the products.
    While the most common way to do this is by defining a factory method per
    product, if many product families are possible then the ConcreteFactory
    can be implemented using the Prototype pattern.
    """
    @staticmethod
    def make_random_drink():
        return Drink()


class BeerFactory(DrinkFactory):
    """
    Concrete Factory
    Implements the operations to create concrete product objects.

    An application typically needs only one instance of a ConcreteFactory per
    product family, so it's usually best implemented as a Singleton but this
    will be left as an excercise to the reader.

    These Concrete Factories are implemented using the Factory Method pattern.
    """
    @staticmethod
    def make_random_drink():
        name = random.choice([Heineken, Sapporo])
        return name()


class SodaFactory(DrinkFactory):
    """Concrete Factory"""
    @staticmethod
    def make_random_drink():
        name = random.choice([MelonSoda, Ramune])
        return name()


class Drink:
    """
    Abstract Product
    Declares an interface for a type of product object.
    """
    def __init__(self):
        self._size  = None

    def get_size(self):
        return self._size


class MelonSoda(Drink):
    """
    Concrete Product
    1. Implements the Abstract Product interface.
    2. Defines a product object to be created by the corresponding concrete
       factory.
    """
    def __init__(self):
        self._size = 10

    def __str__(self):
        return "Melon Soda"


class Ramune(Drink):
    """Concrete Product"""
    def __init__(self):
        self._size = 6.76

    def __str__(self):
        return "Ramune"


class Heineken(Drink):
    """Concrete Product"""
    def __init__(self):
        self._size = 24

    def __str__(self):
        return "Heineken"


class Sapporo(Drink):
    """Concrete Product"""
    def __init__(self):
        self._size = 22

    def __str__(self):
        return "Sapporo"


class Client:
    """
    Client
    Uses only interfaces declared by the Abstract Factory
    and Abstract Product classes.
    """
    def main(self):
        for i in range(5):
            # Normally a single instance of a ConcreteFactory class is created
            # at run-time. This concrete factory creates product objects having
            # a particular implementation. To create different product objects,
            # clients should use a different concrete factories.
            factory = random.choice([BeerFactory, SodaFactory])

            # AbstractFactory defers creation of product objects to its
            # ConcreteFactory subclass.
            drink = factory.make_random_drink()
            print "%10s: %s oz" % (drink, drink.get_size())


if __name__ == "__main__":
    client = Client()
    client.main()
