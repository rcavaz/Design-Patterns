# [Design Patterns](../README.md)
## [Behavioral Patterns](./behavioral.md)
### Memento Pattern

#### Motivation
It is sometimes necessary to capture the internal state of an object at some point and have the ability to restore the object to that state later in time. Such a case is useful in case of error or failure. Consider the case of a calculator object with an undo operation such a calculator could simply maintain a list of all previous operation that it has performed and thus would be able to restore a previous calculation it has performed. This would cause the calculator object to become larger, more complex, and heavyweight, as the calculator object would have to provide additional undo functionality and should maintain a list of all previous operations. This functionality can be moved out of the calculator class, so that an external (let's call it undo manager class) can collect the internal state of the calculator and save it. However providing the explicit access to every state variable of the calculator to the restore manager would be impractical and would violate the encapsulation principle.

#### Intent
The intent of this pattern is to capture the internal state of an object without violating encapsulation and thus providing a mean for restoring the object into initial state when needed.


#### Applicability & Examples

![Memento](../uml/memento.png)

| Language                               | Example |
| :------------------------------------: | ------- |
| [python](./python3/behavioral/memento) | [undo](./python3/behavioral/memento/undo.py)

#### Specific problems and implementation consecuences

#### Related Patterns

#### Known Uses
