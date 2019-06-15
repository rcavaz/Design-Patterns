# [Design Patterns](../README.md)
## [Behavioral Patterns](./behavioral.md)
### Command Pattern

Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

#### Motivation

Sometimes it's necessary to issue requests to objects without knowing anything about the operation being requested or the receiver of the request. For example, user interface toolkits include objects like buttons and menus that carry out a request in response to user input. But the toolkit can't implement the request explicitly in the button or menu, because only applications that use the toolkit know what should be done on which object. As toolkit designers we have no way of knowing the receiver of the request or the operations that will carry it out.

The Command pattern lets toolkit objects make requests of unspecified application objects by turning the request itself into an object. This object can be stored and passed around like other objects. The key to this pattern is an abstract Command class, which declares an interface for executing operations. In the simplest form this interface includes an abstract Execute operation. Concrete Command subclasses specify a receiver-action pair by storing the receiver as an instance variable and by implementing Execute to invoke the request. The receiver has the knowledge required to carry out the request.

#### Implementation & Examples

![Command](../uml/command.png)

| Language                                | Example |
| :-------------------------------------: | ------- |
| [python](../python3/behavioral/command) | [Framework](../python3/behavioral/command/?.py)

#### Specific problems and implementation consecuences

#### Related Patterns
* [Composite](./composite.md) - A Composite can be used to implement MacroCommands.
* [Memento](./memento.md) - A Memento can keep state the command requires to undo its effect.
* [Prototype](./prototype.md) - A command that must be copied before being placed on the historylist acts as a Prototype.
