# [Design Patterns](../../../README.md)
## [Behavioral Patterns](../../../readmes/behavioral.md)
### Chain of Responsibility Pattern

![Chain of Responsibility](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/rcavaz/Design-Patterns/feature/python/uml/chain.uml)

```python
class Handler(ABC):

    def __init__(self, successor=None):
        self.__successor = successor

    @abstractmethod
    def handle_request(self):
        pass
```
* Defines an interface for handling requests.

```python
class ConcreteHandler(Handler):

    def handle_request(self, request):
        if can_handle:
            # Handling block ...
        elif self.__successor is not None:
            return self.__successor.handle_request(request)
```
* Handles the requests it is responsible for.
  * If it can't handle it, it sends it to its successor.

```python
class Client:

    def action_1(self, request):
        h = ConcreteHandler()
        return h.handle_request(request)

    def action_2(self, request):
        h1 = ConcreteHandler1()
        h2 = ConcreteHandler2(h1)
        return h2.handle_request(request)
```
* Sends commands to the root of the chain.

### Examples
1. [Pipeline](./pipeline.py) - Defer numeric system conversion to successors.

#### Related Patterns
* [Command](../command) - Chain of Responsibility can use Command to represent requests as objects.
* [Composite](../composite) - Component parents can act as successors.
