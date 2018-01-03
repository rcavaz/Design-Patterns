#!/usr/bin/env python
"""
ABSTRACT FACTORY (a.k.a. Kit)

Use the Abstract Factory pattern when:
    1. a system should be independent of how its products are created,
       composed and represented.
    2. a system should be configured with one of the multiple families of products.
    3. a family of related product objects is designed to be used together,
       and you need to enforce this constraint.
    4. you want to provide a class library of products, and you want to reveal
       just their interfaces, not their implementations.
"""
import random

class DrinkFactory(object):
    """
    Abstract Factory
    Declares an interface for operations that create abstract product objects.
    """
    @staticmethod
    def make_drink(name):
        return Drink()

    @staticmethod
    def make_random():
        return Drink()


class BeerFactory(DrinkFactory):
    """
    Concrete Factory
    Implements the operations to create concrete product objects.
    """
    @staticmethod
    def make_drink(name):
        if name == "Heineken":
            return Heineken()
        elif name == "Sapporo":
            return Sapporo()

    @staticmethod
    def make_random():
        name = random.choice([Heineken, Sapporo])
        return name()


class SodaFactory(DrinkFactory):
    """Concrete Factory"""
    @staticmethod
    def make_drink(name):
        if name == "Melon Soda":
            return MelonSoda()
        elif name == "Ramune":
            return Ramune()

    @staticmethod
    def make_random():
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
    2. Defines a product object to be created by the corresponding concrete factory.
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


if __name__ == "__main__":
    """
    Client
    Uses only interfaces declared by the Abstract Factory and Abstract Product classes.
    """

    for i in range(5):
        factory = random.choice([BeerFactory, SodaFactory])
        drink = factory.make_random()
        print "%s: %s" % (drink, drink.get_size())
