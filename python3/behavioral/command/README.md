# [Design Patterns](../../../README.md)
## [Behavioral Patterns](../../../readmes/behavioral.md)
### Command Pattern

![Command](../../../uml/command.png)

```
class Receiver:

    def action(self):
        pass
```
* Knows how to perform the operations associated with carrying out a request.
* Any class may serve as a Receiver

```
class Command(ABC):

    def __init__(self, receiver):
        self.__receiver = receiver
        self.__state = None

    @abstractmethod
    def execute(self):
        pass
```
* Declares an interface for executing an operation.

```
class ConcreteCommand(Command):

    def execute(self):
        return self.__receiver.action()
```
* Defines a binding between a Receiver object and an action.
* Implements execute() by invoking the corresponding operation(s) on Receiver.

```
class Invoker:

    def __init__(self):
        self.__command = None

    def store_command(self, command):
        assert isinstance(command, Command)
        self.__command = command

    def operation(self):
        return self.__command.execute()
```
* Asks the command to carry out the request.

```
class Client:

    def __init__(self, invoker):
        receiver = Receiver()
        command = ConcreteCommand(receiver)
        invoker.store_command(command)
```
* Creates a ConcreteCommand object and sets its receiver.

### Examples
1. Callbacks
2. Undo/Redo

#### Related Patterns
1. [Memento](../memento) - ...
2. [Composite](../composite) - ...

