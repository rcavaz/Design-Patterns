# Design-Patterns
This is a collection of software design patterns from the well known "Design Patterns : Elements of Reusable Object-Oriented Software" book implemented in a number of languages (currently only python).

The main motivation for this proyect is for people to learn and compare programming languages while implementing these software patterns.

The code implementations differ from the book and include documentation specific to the language being used. To find a specific language implementation search for the 'Examples' section on each pattern page, right below the UML diagram.

## [Behavioral](./readmes/behavioral.md)
Pattern                                       | Intent | UML
:-------------------------------------------: | ------ | ------
[Chain of Responsibility](./readmes/chain.md) | Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. | ![Chain of Responsibility](./uml/chain.png)
[Command](./readmes/command.md)               | Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations. | ![Command](./uml/command.png)
[Interpreter](./readmes/interpreter.md)       | Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language. | ![Interpreter](./uml/interpreter.png)
[Iterator](./readmes/iterator.md)             | Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation. | ![Iterator](./uml/iterator.png)
[Mediator](./readmes/mediator.md)             | Define an object that encapsulates how a set of objects interact. | ![Mediator](./uml/mediator.png)
[Memento](./readmes/memento.md)               | Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later. | ![Memento](./uml/memento.png)
[Observer](./readmes/observer.md)             | Define a one-to-many dependency between objects so that when an object changes state, all its dependents are notified and updated automatically. | ![Observer](./uml/observer.png)
[State](./readmes/state.md)                   | Allow an object to alter its behavior when its internal state changes. The object will appear to change its class. | ![State](./uml/state.png)
[Strategy](./readmes/strategy.md)             | Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it. | ![Strategy](./uml/strategy.png)
[Template Method](./readmes/template.md)      | Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. | ![Template Method](./uml/template.png)
[Visitor](./readmes/visitor.md)               | Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates. | ![Visitor](./uml/visitor.png)

## [Creational](./readmes/creational.md)
Pattern          | Intent | UML
:---------------------------------------: | ------ | ------
[Singleton](./readmes/singleton.md)       | Ensure a class has only one instance, and provide a global point of access to it. | ![Singleton](./uml/singleton.png)
[Factory Method](./readmes/factory.md)    | Define an interface for creating an object, but let subclasses decide which class to instantiate. | ![Factory Method](./uml/factory.png)
[Abstract Factory](./readmes/abstract.md) | Provide an interface for creating families of related or dependent objects without specifying their concrete classes. | ![Abstract Factory](./uml/abstract.png)
[Prototype](./readmes/prototype.md)       | Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype. | ![Prototype](./uml/prototype.png)
[Builder](./readmes/builder.md)           | Separate the construction of a complex object from its representation so that the same construction process can create different representations. | ![Builder](./uml/builder.png)

## [Structural](./readmes/structural.md)
Pattern                             | Intent | UML
:---------------------------------: | ------ | ------
[Adapter](./readmes/adapter.md)     | Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces. | ![Adapter](./uml/adapter.png)
[Bridge](./readmes/bridge.md)       | Decouple an abstraction from its implementation so that the two can vary independently. | ![Bridge](./uml/bridge.png)
[Composite](./readmes/composite.md) | Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly. | ![Composite](./uml/composite.png)
[Decorator](./readmes/decorator.md) | Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality. | ![Decorator](./uml/decorator.png)
[Facade](./readmes/facade.md)       | Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use. | ![Facade](./uml/facade.png)
[Flyweight](./readmes/flyweight.md) | Use sharing to support large numbers of fine-grained objects efficiently. | ![Flyweight](./uml/flyweight.png)
[Proxy](./readmes/proxy.md)         | Provide a surrogate or placeholder for another object to control access to it. | ![Proxy](./uml/proxy.png)

## References
1. Gamma, Erich, et al. Design Patterns : Elements of Reusable Object-Oriented Software. Machinery Industry, 2003.
