# [Design Patterns](../README.md)
## [Behavioral Patterns](./behavioral.md)
### Memento Pattern

Without violating encapsulation, capture and externalize an object's internal state in order to restore it later.

#### Motivation
There are times when we want to have the ability to restore an object to a previous state. Such is the case for error or failure recovery, or supporting "undo" operations. But providing explicit access to every state variable is impractical and would violate the encapsulation principle.

#### Implementation & Examples

![Memento](../uml/memento.png)

| Language                                | Example |
| :-------------------------------------: | ------- |
| [python](../python3/behavioral/memento) | [Fibonacci](../python3/behavioral/memento/fibo.py)

#### Specific problems and implementation consecuences

#### Related Patterns
* [Command Pattern](./command.md) - Commands can make use of mementos to support undoable operations.

#### Known Uses
* Database Transactions
* Undo/Restore operations
