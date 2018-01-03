#!/usr/bin/env python
"""
BUILDER

Use the Builder pattern when:
    1. the algorithm for creating a complex object should be independent of
       the parts that make up the object and how they're assembled.
    2. the construction process must allow different representations for the
       object that's constructed.
"""
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


class ForgeSword(Forge):
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


import random

if __name__ == "__main__":
    item = random.choice(["Jagdkommando","Katana","Santoku","Zweihander"])
    director = Blacksmith()
    director.builder = ForgeSword()
    product = director.build(item)
    product.specification()
