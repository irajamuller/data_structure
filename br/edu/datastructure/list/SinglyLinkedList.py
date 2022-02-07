from Exceptions import UnderflowError
from ADTList import ADTList
from Node import Node

class SinglyLinkedList(ADTList):
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

    def insert_first(self, element: object) -> None:
        new_node: Node = Node(element)
        if self.is_empty():
            self._first = self._last = new_node
        else:
            new_node.next = self._first
            self._first = new_node
        self._count += 1

    def insert_last(self, element: object) -> None:
        new_node: Node = Node(element)
        if self.is_empty():
            self._first = self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._count += 1

    def insert(self, element: object, pos: int) -> None:
        if (pos < 0 or pos > self._count):
            raise IndexError()

        if pos == 0:
            self.insert_first(element)
        elif pos == self._count:
            self.insert_last(element)
        else:
            prev: Node = self._first
            for _ in range(0, pos - 1):
                prev = prev.next

            new_node: Node = Node(element)
            new_node.next = prev.next
            prev.next = new_node
            self._count += 1

    def remove(self, pos: int) -> object:
        if self.is_empty():
            raise UnderflowError()
        if (pos < 0 or pos >= self._count):
            raise IndexError()
        if pos == 0:
            self.remove_first()
        elif pos == self._count:
            self.remove_last()
        else:
            prev: Node = self._first
            for _ in range(0, pos - 1):
                prev = prev.next
            element: object = prev.next.element
            prev.next = prev.next.next
            self._count -= 1
            return element

    def remove_first(self) -> object:
        if self.is_empty():
            raise UnderflowError()

        element: object = self._first.element
        if (self._first == self._last):
            self._first = self._last = None
        else:
            self._first = self._first.next
        self._count -= 1
        return element

    def remove_last(self) -> object:
        if self.is_empty():
            raise UnderflowError()

        element: object = self._last.element
        if (self._first == self._last):
            self._first = self._last = None
        else:
            prev: Node = self._first
            while (prev.next != self._last):
                prev = prev.next
            self._last = prev
            prev.next = None
        self._count -= 1
        return element

    def search(self, element: object) -> int:
        for i, elm in enumerate(self):
            if elm == element:
                return i
        return -1

    def get(self, pos: int) -> object:
        if (pos < 0 or pos >= self._count):
            raise IndexError()
        current: Node = self._first
        for _ in range(0, pos):
            current = current.next
        return current.element

    def size(self) -> int:
        return len(self)