from ADTStack import ADTStack
from Node import Node
from Exceptions import UnderflowError

class UnboundedLinkedStack(ADTStack):
    def __init__(self) -> None:
        self._top: Node = None
        self._count: int = 0

    def __len__(self) -> int:
        return self._count

    def __str__(self) -> str:
        return "[" + " ".join([str(node) for node in self]) + "]"

    def __iter__(self) -> object:
        current: Node = self._top
        while current:
            yield current.element
            current = current.next

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return False

    def push(self, element: object) -> None:
        new_node: Node = Node(element)
        new_node.next = self._top
        self._top = new_node
        self._count += 1

    def pop(self) -> object:
        if self.isEmpty():
            raise UnderflowError()
        element: object = self._top.element
        self._top = self._top.next
        self._count -= 1
        return element

    def peek(self) -> object:
        if self.isEmpty():
            raise UnderflowError()
        return self._top.element

    def size(self) -> int:
        return len(self)