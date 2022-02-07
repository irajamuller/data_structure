from xml.sax import make_parser
import numpy as np
from Exceptions import UnderflowError
from ADTQueue import ADTQueue

class UnboundedArrayQueue(ADTQueue):
    def __init__(self, size: int = ADTQueue.DEFAULT_SIZE) -> None:
        self._last: int = -1
        self._elements = np.empty(size, object)

    def __len__(self) -> int:
        return self._last + 1

    def __str__(self) -> str:
        return "[" + " ".join([str(elm) for elm in self]) + "]"

    def __iter__(self) -> object:
        for elm in self._elements[:self._last + 1]:
            yield elm

    def is_empty(self) -> bool:
        return self._last == -1

    def is_full(self) -> bool:
        return False

    def enqueue(self, element: object) -> None:
        if self.size() == len(self._elements):
            self._elements = np.concatenate((self._elements, 
                             np.empty(len(self._elements), object)))
        self._last += 1
        self._elements[self._last] = element

    def dequeue(self) -> object:
        if self.is_empty():
            raise UnderflowError()
        element: object = self._elements[0]
        self._last -= 1
        self._elements = np.concatenate((self._elements[1:], np.empty(1, object)))
        return element
    
    def peek(self) -> object:
        if self.is_empty():
            raise UnderflowError()
        return self._elements[0]

    def size(self) -> int:
        return len(self)