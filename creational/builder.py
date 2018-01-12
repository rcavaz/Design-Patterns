#!/usr/bin/env python
"""
BUILDER

Use the Builder pattern when:
    1. the algorithm for creating a complex object should be independent of
       the parts that make up the object and how they're assembled.
    2. the construction process must allow different representations for the
       object that's constructed.


Implementation:

    Suppose we want to be able to construct many different representations of
    knife or sword objects which all have the following common parts:
        1) a Blade, which could have between 1 and 3 edges;
        2) a Cross Guard (optional),
        3) a Grip,
        4) and a Pommel (optional).

    All these three parts may vary in length and size.
    We will define only 4 of the many possible representations that can be
    made out of the combinations of these parts, which are:
        a) Jagdkommando, a knife will 3 blades.
        b) Santoku, an all purpose kitchen knife.
        c) Katana, a one edged sword.
        d) Zweihander, a big 2 edged sword.


    We will create a Builder class called Forge which will define our interface
    for creating the parts of our products.

    Then we will create a Concrete Builder class called ForgeCutlery which will
    be responsible of assembling the parts of the product.

    Next we will create a Director class called Blacksmith who will know the
    construction steps for each of our Cutlery products.

    After this we will create Product classes Knife and Sword which will
    define interfaces for assembling the parts.

    Then we will create Product Part classes for each of the 4 possible parts
    the products might be made of.

    Finally we will create a Client class that will create an instance of our
    Blacksmith director, configure it to build a cutlery product, and randomly
    request the creation of one of the many representations defined.
"""
import random


class Forge(object):
    """
    Builder
    Specifies an abstract interface for creating parts of a Product object.
    """
    def __init__(self):
        self.item = None

    def build(self, item, kind):
        if item == "knife":
            self.item = Knife(kind)
        elif item == "sword":
            self.item = Sword(kind)
        else:
            raise NotImplementedError("Don't know how to make '%s'" % item)

    def build_blade(self, attr):
        raise NotImplementedError

    def build_cross_guard(self, attr):
        raise NotImplementedError

    def build_grip(self, attr):
        raise NotImplementedError

    def build_pommel(self, attr):
        raise NotImplementedError


class ForgeCutlery(Forge):
    """
    Concrete Builder
    1. Constructs and assembles parts of the product by implementing the
       Builder interface.
    2. Defines and keeps track of the representation it creates.
    3. Provides an interface for retrieving the product.
    """
    def build_blade(self, attr):
        blade = Blade()
        for k, v in attr.iteritems():
            setattr(blade, k, v)
        self.item.setBlade(blade)

    def build_cross_guard(self, attr):
        guard = CrossGuard()
        for k, v in attr.iteritems():
            setattr(guard, k, v)
        self.item.setCrossGuard(guard)

    def build_grip(self, attr):
        grip = Grip()
        for k, v in  attr.iteritems():
            setattr(grip, k, v)
        self.item.setGrip(grip)

    def build_pommel(self, attr):
        pommel = Pommel()
        for k, v in  attr.iteritems():
            setattr(pommel, k, v)
        self.item.setPommel(pommel)

    def get_sword(self):
        return self.item


class Blacksmith:
    """
    Director
    Constructs an object using the Builder interface.
    """
    def __init__(self):
        self.builder = None

    def setBuilder(self, builder):
        self.builder = builder

    def build(self, item):
        if item == "Jagdkommando":
            return self.build_Jagdkommando()
        elif item == "Santoku":
            return self.build_Santoku()
        elif item == "Katana":
            return self.build_Katana()
        elif item == "Zweihander":
            return self.build_Zweihander()
        else:
            raise NotImplementedError("Don't know how to build %s" % item)

    def build_Jagdkommando(self):
        self.builder.build("knife", "Jagdkommando")

        specs = {'edges'   : 3
                ,'is_sharp': True
                ,'length'  : 1
                ,'weight'  : 2.5}
        self.builder.build_blade(specs)

        specs = {'length'  : 1
                ,'weight'  : 1}
        self.builder.build_grip(specs)

        return self.builder.get_sword()

    def build_Santoku(self):
        self.builder.build("knife", "Santoku")

        specs = {'edges'   : 1
                ,'is_sharp': True
                ,'length'  : 1
                ,'weight'  : 1}
        self.builder.build_blade(specs)

        specs = {'length'  : 1
                ,'weight'  : 1}
        self.builder.build_grip(specs)

        return self.builder.get_sword()

    def build_Katana(self):
        self.builder.build("sword", "Katana")

        specs = {'edges'   : 1
                ,'is_sharp': True
                ,'length'  : 7
                ,'weight'  : 3}
        self.builder.build_blade(specs)

        specs = {'length'  : 1
                ,'weight'  : 0.1}
        self.builder.build_cross_guard(specs)

        specs = {'length'  : 2
                ,'weight'  : 2}
        self.builder.build_grip(specs)

        return self.builder.get_sword()

    def build_Zweihander(self):
        self.builder.build("sword", "Zweihander")

        specs = {'edges'   : 2
                ,'is_sharp': True
                ,'length'  : 3
                ,'weight'  : 3}
        self.builder.build_blade(specs)

        specs = {'length'  : 3
                ,'weight'  : 3}
        self.builder.build_cross_guard(specs)

        specs = {'length'  : 10
                ,'weight'  : 5}
        self.builder.build_grip(specs)

        specs = {'length'  : 0.1
                ,'weight'  : 3}
        self.builder.build_pommel(specs)

        return self.builder.get_sword()


class Knife(object):
    """
    Product
    1. Represents the complex object under construction.
       Concrete Builder builds the product's internal representation and
       defines the process by which it's assembled.
    2. Includes classes that define the constituent parts, including
       interfaces for assembling the parts into the final result.
    """
    def __init__(self, kind):
        self.__blade  = None
        self.__grip   = None
        self.kind     = kind

    def setBlade(self, blade):
        self.__blade = blade

    def setGrip(self, grip):
        self.__grip = grip

    def specification(self):
        print '%s - Specification' % self.kind
        print 'Blade:'
        print '  - edges: %s' % self.__blade.edges
        print '  - is_sharp: %s' % self.__blade.is_sharp
        print '  - length: %s' % self.__blade.length
        print '  - weight: %s' % self.__blade.weight
        print 'Grip:'
        print '  - length: %s' % self.__grip.length
        print '  - weight: %s' % self.__grip.weight


class Sword(object):
    """Product"""
    def __init__(self, kind):
        self.__blade  = None
        self.__grip   = None
        self.__guard  = None
        self.kind     = kind
        self.__pommel = None

    def setBlade(self, blade):
        self.__blade = blade

    def setCrossGuard(self, guard):
        self.__guard = guard

    def setGrip(self, grip):
        self.__grip = grip

    def setPommel(self, pommel):
        self.__pommel = pommel

    def specification(self):
        print '%s - Specification' % self.kind
        print 'Blade:'
        print '  - edges: %s' % self.__blade.edges
        print '  - is_sharp: %s' % self.__blade.is_sharp
        print '  - length: %s' % self.__blade.length
        print '  - weight: %s' % self.__blade.weight
        if self.__guard is not None:
            print 'Cross Guard:'
            print '  - length: %s' % self.__guard.length
            print '  - weight: %s' % self.__guard.weight
        print 'Grip:'
        print '  - length: %s' % self.__grip.length
        print '  - weight: %s' % self.__grip.weight
        if self.__pommel is not None:
            print 'Pommel:'
            print '  - length: %s' % self.__pommel.length
            print '  - weight: %s' % self.__pommel.weight


class Blade:
    """
    Product Part
    Individual elements that constitute a whole product.
    """
    def __init__(self):
        self.edges    = None
        self.is_sharp = False
        self.length   = None
        self.weight   = None


class CrossGuard:
    """Product Part"""
    def __init__(self):
        self.length = None
        self.model  = None
        self.weight = None


class Grip:
    """Product Part"""
    def __init__(self):
        self.length = None
        self.size   = None
        self.weight = None


class Pommel:
    """Product Part"""
    def __init__(self):
        self.length = None
        self.model  = None
        self.weight = None


class Client:
    def main(self):
        item = random.choice(["Jagdkommando","Katana","Santoku","Zweihander"])

        # The client creates the Director object and configures it with the
        # desired Builder object.
        director = Blacksmith()
        director.builder = ForgeCutlery()

        # Director notifies the builder whenever a part of the product should
        # be built while Builder handles requests from the director and adds
        # parts to the product. Finally, the client retrieves the product from
        # the builder.
        product = director.build(item)
        product.specification()


if __name__ == "__main__":
    client = Client()
    client.main()
