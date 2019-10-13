# Design-Patterns
This is a collection of software design patterns from the well known "Design Patterns : Elements of Reusable Object-Oriented Software" book implemented in python.

The main motivation for this proyect is for people to learn and compare programming languages while implementing these software patterns.

The code implementations differ from the book and include documentation specific to the language being used. To find a specific language implementation search for the 'Examples' section on each pattern page, right below the UML diagram.

## Clasification

### Class

Patterns that apply primarily to classes.

Creational           | Structural   | Behavioral
:------------------: | ------------ | -------------------
[Factory Method][10] | [Adapter][2] | [Interpreter][12]
|                    |              | [Template Method][22]

### Object

Patterns that apply primarily to objects.

Creational             | Structural      | Behavioral
:--------------------: | --------------- | ---------
[Abstract Factory][1]  | [Adapter][2]    | [Chain of Responsibility][5]
[Builder][4]           | [Bridge][3]     | [Command][6]
[Prototype][17]        | [Composite][7]  | [Iterator][13]
[Singleton][19]        | [Decorator][8]  | [Mediator][14]
|                      | [Facade][9]     | [Memento][15]
|                      | [Flyweight][11] | [Observer][16]
|                      | [Proxy][18]     | [State][20]
|                      |                 | [Strategy][21]
|                      |                 | [Visitor][23]


## [Behavioral](./readmes/behavioral.md)
Pattern                      | Intent | UML
:--------------------------: | ------ | ------
[Chain of Responsibility][5] | Object can fullfill a request.                                 | ![Chain of Responsibility][28]
[Command][6]                 | When and how a request is fullfilled.                          | ![Command][29]
[Interpreter][12]            | Grammar and interpretation of a language.                      | ![Interpreter][35]
[Iterator][13]               | How an aggregate's elements are traversed.                     | ![Iterator][36]
[Mediator][14]               | How and which objects interact with each other.                | ![Mediator][37]
[Memento][15]                | What and when private information is stored outside an object. | ![Memento][38]
[Observer][16]               | How dependent objects stay up to date.                         | ![Observer][39]
[State][20]                  | States of an object.                                           | ![State][43]
[Strategy][21]               | An algorithm.                                                  | ![Strategy][44]
[Template Method][22]        | Steps of an algorithm.                                         | ![Template Method][45]
[Visitor][23]                | Apply operation to objects without changing its class(es).     | ![Visitor][46]

## [Creational](./readmes/creational.md)
Pattern          | Intent | UML
:-------------------: | ------ | ------
[Abstract Factory][1] | Families of product objects.             | ![Abstract Factory][24]
[Builder][4]          | How a composite object gets created.     | ![Builder][27]
[Factory Method][10]  | Subclass of object that is instantiated. | ![Factory Method][33]
[Prototype][17]       | Class of object that is instantiated.    | ![Prototype][40]
[Singleton][19]       | The sole instance of a class.            | ![Singleton][42]

## [Structural](./readmes/structural.md)
Pattern                             | Intent | UML
:-------------: | ------ | ------
[Adapter][2]    | Interface of an object.                        | ![Adapter][25]
[Bridge][3]     | Implementation of an object.                   | ![Bridge][26]
[Composite][7]  | Structure and composition without subclassing. | ![Composite][30]
[Decorator][8]  | Responsibilities without subclassing.          | ![Decorator][31]
[Facade][9]     | Interface to a subsystem.                      | ![Facade][32]
[Flyweight][11] | Storage costs of objects.                      | ![Flyweight][34]
[Proxy][18]     | How an object's location is accessed.          | ![Proxy][41]


[1]: ./readmes/abstract.md
[2]: ./readmes/adapter.md
[3]: ./readmes/bridge.md
[4]: ./readmes/builder.md
[5]: ./readmes/chain.md
[6]: ./readmes/command.md
[7]: ./readmes/composite.md
[8]: ./readmes/decorator.md
[9]: ./readmes/facade.md
[10]: ./readmes/factory.md
[11]: ./readmes/flyweight.md
[12]: ./readmes/interpreter.md
[13]: ./readmes/iterator.md
[14]: ./readmes/mediator.md
[15]: ./readmes/memento.md
[16]: ./readmes/observer.md
[17]: ./readmes/prototype.md
[18]: ./readmes/proxy.md
[19]: ./readmes/singleton.md
[20]: ./readmes/state.md
[21]: ./readmes/strategy.md
[22]: ./readmes/template.md
[23]: ./readmes/visitor.md

[24]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/abstract.uml
[25]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/adapter.uml
[26]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/bridge.uml
[27]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/builder.uml
[28]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/chain.uml
[29]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/command.uml
[30]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/composite.uml
[31]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/decorator.uml
[32]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/facade.uml
[33]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/factory.uml
[34]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/flyweight.uml
[35]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/interpreter.uml
[36]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/iterator.uml
[37]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/mediator.uml
[38]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/memento.uml
[39]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/observer.uml
[40]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/prototype.uml
[41]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/proxy.uml
[42]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/singleton.uml
[43]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/state.uml
[44]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/strategy.uml
[45]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/template.uml
[46]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/visitor.uml

## References
1. Gamma, Erich, et al. Design Patterns : Elements of Reusable Object-Oriented Software. Machinery Industry, 2003.
