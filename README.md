# Design-Patterns
This is a collection of software design patterns from the well known "Design Patterns : Elements of Reusable Object-Oriented Software" book implemented in python.

The main motivation for this proyect is for people to learn and compare programming languages while implementing these software patterns.

The code implementations differ from the book and include documentation specific to the language being used. To find a specific language implementation search for the 'Examples' section on each pattern page, right below the UML diagram.

## Clasification

### Class

Patterns that apply primarily to classes.

[Creational][2]      | [Structural][3] | [Behavioral][1]
:------------------: | --------------- | -------------------
[Factory Method][13] | [Adapter][5]    | [Interpreter][15]
|                    |                 | [Template Method][25]

### Object

Patterns that apply primarily to objects.

[Creational][2]        | [Structural][3] | [Behavioral][1]
:--------------------: | --------------- | -------------------
[Abstract Factory][4]  | [Adapter][5]    | [Chain of Responsibility][8]
[Builder][7]           | [Bridge][6]     | [Command][9]
[Prototype][20]        | [Composite][10] | [Iterator][16]
[Singleton][22]        | [Decorator][11] | [Mediator][17]
|                      | [Facade][12]    | [Memento][18]
|                      | [Flyweight][14] | [Observer][19]
|                      | [Proxy][21]     | [State][23]
|                      |                 | [Strategy][24]
|                      |                 | [Visitor][26]


## [Behavioral][1]
Pattern                      | Intent | UML
:--------------------------: | ------ | ------
[Chain of Responsibility][8] | Object can fullfill a request.                                 | ![Chain of Responsibility][31]
[Command][9]                 | When and how a request is fullfilled.                          | ![Command][32]
[Interpreter][15]            | Grammar and interpretation of a language.                      | ![Interpreter][38]
[Iterator][16]               | How an aggregate's elements are traversed.                     | ![Iterator][39]
[Mediator][17]               | How and which objects interact with each other.                | ![Mediator][40]
[Memento][18]                | What and when private information is stored outside an object. | ![Memento][41]
[Observer][19]               | How dependent objects stay up to date.                         | ![Observer][42]
[State][23]                  | States of an object.                                           | ![State][46]
[Strategy][24]               | An algorithm.                                                  | ![Strategy][47]
[Template Method][25]        | Steps of an algorithm.                                         | ![Template Method][48]
[Visitor][26]                | Apply operation to objects without changing its class(es).     | ![Visitor][49]

## [Creational][2]
Pattern          | Intent | UML
:-------------------: | ------ | ------
[Abstract Factory][4] | Families of product objects.             | ![Abstract Factory][27]
[Builder][7]          | How a composite object gets created.     | ![Builder][30]
[Factory Method][13]  | Subclass of object that is instantiated. | ![Factory Method][36]
[Prototype][20]       | Class of object that is instantiated.    | ![Prototype][43]
[Singleton][22]       | The sole instance of a class.            | ![Singleton][45]

## [Structural][3]
Pattern                             | Intent | UML
:-------------: | ------ | ------
[Adapter][5]    | Interface of an object.                        | ![Adapter][28]
[Bridge][6]     | Implementation of an object.                   | ![Bridge][29]
[Composite][10]  | Structure and composition without subclassing. | ![Composite][33]
[Decorator][11]  | Responsibilities without subclassing.          | ![Decorator][34]
[Facade][12]     | Interface to a subsystem.                      | ![Facade][35]
[Flyweight][14] | Storage costs of objects.                      | ![Flyweight][37]
[Proxy][21]     | How an object's location is accessed.          | ![Proxy][44]

[1]: ./readmes/behavioral.md
[2]: ./readmes/creational.md
[3]: ./readmes/structural.md

[4]: ./readmes/abstract.md
[5]: ./readmes/adapter.md
[6]: ./readmes/bridge.md
[7]: ./readmes/builder.md
[8]: ./readmes/chain.md
[9]: ./readmes/command.md
[10]: ./readmes/composite.md
[11]: ./readmes/decorator.md
[12]: ./readmes/facade.md
[13]: ./readmes/factory.md
[14]: ./readmes/flyweight.md
[15]: ./readmes/interpreter.md
[16]: ./readmes/iterator.md
[17]: ./readmes/mediator.md
[18]: ./readmes/memento.md
[19]: ./readmes/observer.md
[20]: ./readmes/prototype.md
[21]: ./readmes/proxy.md
[22]: ./readmes/singleton.md
[23]: ./readmes/state.md
[24]: ./readmes/strategy.md
[25]: ./readmes/template.md
[26]: ./readmes/visitor.md

[27]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/abstract.uml
[28]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/adapter.uml
[29]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/bridge.uml
[30]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/builder.uml
[31]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/chain.uml
[32]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/command.uml
[33]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/composite.uml
[34]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/decorator.uml
[35]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/facade.uml
[36]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/factory.uml
[37]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/flyweight.uml
[38]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/interpreter.uml
[39]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/iterator.uml
[40]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/mediator.uml
[41]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/memento.uml
[42]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/observer.uml
[43]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/prototype.uml
[44]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/proxy.uml
[45]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/singleton.uml
[46]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/state.uml
[47]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/strategy.uml
[48]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/template.uml
[49]: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/visitor.uml

## References
1. Gamma, Erich, et al. Design Patterns : Elements of Reusable Object-Oriented Software. Machinery Industry, 2003.
