# Design-Patterns
A collection of software design patterns from the well known "Design Patterns : Elements of Reusable Object-Oriented Software" book implemented in various langagues.

The code implementations differ from those from the book and include inline documentation sepecific to the language being used.

## [Creational](./creational/README.md)
Pattern          | Intent
:--------------: | ------
Singleton        | Ensure a class has only one instance, and provide a global point of access to it.
Factory Method   | Define an interface for creating an object, but let subclasses decide which class to instantiate.
Abstract Factory | Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
Prototype        | Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.
Builder          | Separate the construction of a complex object from its representation so that the same construction process can create different representations.

## [Structural](./structural/README.md)
Pattern   | Intent
:-------: | ------
Adapter   | Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.
Bridge    | Decouple an abstraction from its implementation so that the two can vary independently.
Composite | Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
Decorator | Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
Facade    | Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
Flyweight | Use sharing to support large numbers of fine-grained objects efficiently.
Proxy     | Provide a surrogate or placeholder for another object to control access to it.

## References
1. Gamma, Erich, et al. Design Patterns : Elements of Reusable Object-Oriented Software. Machinery Industry, 2003.
