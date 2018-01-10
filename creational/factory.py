#!/usr/bin/env python
"""
FACTORY METHOD (a.k.a. Virtual Constructor)

Use the Factory Method when:
    1. a class can't anticipate the class of objects it must create.
    2. a class wants its subclasses to specify the objects it creates.
    3. classes delegate responsibility to one of several helper subclasses
       and you want to localize the knowledge of which helper subclass is
       the delegate.


Implementation:

    Pretend we have a number of pizza products from which a client may request
    for its prize and we are only interested in creating the objects if needed
    but can't anticipate which one will be required.

    For this we will first create a Product class called Pizza which will
    define the interface of the concrete products.

    Then we will create a Concrete Product class for each of our products.

    Next we will create a Creator class called PizzaFactory which will define
    an interface for creating our products.

    Then we will create a Concrete Creator class called DominosPizzant that
    will implement the factory method.

    Finally we will create a Client class that will rely on its subclasses
    to define the factory method that will return the requested Product.
"""
class Pizza:
    """
    Product
    Defines the interface of objects the factory method creates.
    """
    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price


class MargheritaPizza(Pizza):
    """
    Concrete Product
    Implements the Product interface.
    """
    def __init__(self):
        self._price = 9.5


class PortobelloPizza(Pizza):
    """Concrete Product"""
    def __init__(self):
        self._price = 8.5


class PizzaFactory(object):
    """
    Creator
    1. Declares the factory method which returns an object of type Product.
       Defining a default implementation is optional.
    2. May call the factory method to create a Product object.
    """

    @staticmethod
    def create_pizza(pizza_type):
        """The factory method"""
        return Pizza()

    def get_price(self, pizza_type):
        """An operation that calls the factory method"""
        pizza = self.create_pizza(pizza_type)
        return pizza.get_price()


class DominosPizzant(PizzaFactory):
    """
    Concrete Creator
    Overrides the factory method to return an instance of a Concrete Product.

    Here we choose our factory method 'create_pizza' to be defined as a static
    method because it will never modify neither the class nor the instance.
    """
    @staticmethod
    def create_pizza(pizza_type):
        """The (parameterized) factory method"""
        if pizza_type == 'Margherita':
            return MargheritaPizza()
        elif pizza_type == 'Portobello':
            return PortobelloPizza()
        if pizza_type == 'Hawaiian':
            raise NotImplementedError("Customer taste error!")
        else:
            raise NotImplementedError("Pizza type '%s' not implemented." % pizza_type)


class Client:
    def main(self):
        for pizza_type in ('Margherita', 'Portobello'):
            # Creator relies on its subclasses to define the factory method so
            # that it returns an instance of the appropriate ConcreteProduct.
            #
            # Here we call the factory method indirectly as the object will
            # be short lived.
            print '%s %s' % (pizza_type, DominosPizzant().get_price(pizza_type))

            # Here is how one will call the factory method directly.
            #pizza = DominosPizzant.create_pizza(pizza_type)
            #print '%s %s' % (pizza_type, pizza.get_price())


if __name__ == '__main__':
    client = Client()
    client.main()
