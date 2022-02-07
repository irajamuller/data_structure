from Exceptions import UnderflowError
from ADTQueue import ADTQueue
from Node import Node

class UnboundedLinkedQueue(ADTQueue):
    def __init__(self) -> None:
        self._first: Node = None
        self._last: Node = None
        self._count: int = 0

    def __len__(self) -> int:
        return self._count

    def __str__(self) -> str:
        return "[" + " ".join([str(node) for node in self]) + "]"

    def __iter__(self) -> object:
        current: Node = self._first
        while current:
            yield current.element
            current = current.next

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return False

    def enqueue(self, element: object) -> None:
        new_node: Node = Node(element)
        if self.is_empty():
            self._first = self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._count += 1

    def dequeue(self) -> object:
        if self.is_empty():
            raise UnderflowError()
        element: object = self._last.element
        if self._first == self._last:
            self._first = self._last = None
        else:
            self._first = self._first.next
        self._count -= 1
        return element
    
    def peek(self) -> object:
        if self.is_empty():
            raise UnderflowError()
        return self._first.element

    def size(self) -> int:
        return len(self)