from Exceptions import OverflowError, UnderflowError
from UnboundedArrayQueue import UnboundedArrayQueue
from ADTQueue import ADTQueue

class CircularBoundedArrayQueue(UnboundedArrayQueue):
    def __init__(self, size: int = ADTQueue.DEFAULT_SIZE) -> None:
        super().__init__(size)
        self._first: int = -1
 
    def __str__(self) -> str:
        return "[" + " ".join([str(elm) for elm in self]) + "]"

    def __len__(self) -> int:
        if self.is_empty(): 
            return 0
        else:
            n: int = len(self._elements)
            return (n + self._last - self._first) % n + 1

    def __iter__(self) -> object:
        n: int = self.size()
        for i in range(n):
            k: int = (self._first + i) % len(self._elements)
            yield self._elements[k]

    def is_full(self) -> bool:
        return self._first == (self._last + 1) % len(self._elements)

    def enqueue(self, element: object) -> None:
        if self.is_full():
            raise OverflowError()
        if self._last == -1:
            self._first = self._last = 0
        else:
            self._last = (self._last + 1) % len(self._elements)
        self._elements[self._last] = element

    def dequeue(self) -> object:
        if self.is_empty():
            raise UnderflowError()
        element: object = self._elements[self._first]
        self._elements[self._first] = None
		
        if self._first == self._last:
            self._first = self._last = -1
        else:
            self._first = (self._first + 1) % len(self._elements)
        return element

    def peek(self) -> object:
        if self.is_empty():
            raise UnderflowError()
        return self._elements[self._first]

