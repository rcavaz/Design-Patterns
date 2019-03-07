# [Behavioral Patterns](../../../behavioral.md)
## Memento


```
class Memento:

    def setState(self, state):
        self.serialized_state = SerializedState(state)

    def getState(self):
        return self.serialized_state
```

```
class Originator:

    def __init__(self):
        self.__state = None

    def createMemento(self):
        memento = Memento()
        memento.setState(self.__state)
        return memento

    def setMemento(self, memento):
        self.__state = DeserializeState(memento.getState())

    def operation(self):
        pass
```

```
class CareTaker:

    def main(self):
        o = Originator()
        m = o.createMemento()
        # o.operation1()
        # o.operation2()
        # ...
        o.setMemento(m)
```

Lorem ipsum ...
