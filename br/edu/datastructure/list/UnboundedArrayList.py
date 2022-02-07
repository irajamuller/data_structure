import numpy as np
from ADTList import ADTList
from Exceptions import UnderflowError

class UnboundedArrayList(ADTList):
    def __init__(self, size: int = ADTList.DEFAULT_SIZE) -> None:
        self._elements = np.empty(size, object)
        self._count: int = 0

    def __len__(self) -> int:
        return self._count

    def __str__(self) -> str:
        return "[" + " ".join([str(elm) for elm in self]) + "]"

    def __iter__(self) -> object:
        for elm in self._elements[:self._count]:
            yield elm

    def __ensure_capacity(self) -> None:
        if len(self) == len(self._elements):
            self._elements = np.concatenate((self._elements, 
                             np.empty(len(self._elements), object)))

    def size(self) -> int:
        return len(self)

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return False

    def insert_first(self, element: object) -> None:
        self.insert(element, 0)

    def insert_last(self, element: object) -> None:
        self.insert(element, self._pos)

    def insert(self, element: object, pos: int) -> None:
        if (pos < 0 or pos > self._count):
            raise IndexError()

        self.__ensure_capacity()
        for i in range(self._count - 1, pos - 1, -1):
            self._elements[i + 1] = self._elements[i]
        self._elements[pos] = element
        self._count += 1

    def remove_first(self) -> object:
        self.remove(0)

    def remove_last(self) -> object:
        self.remove_last(self._count - 1)

    def remove(self, pos: int) -> object:
        if self.is_empty():
            raise UnderflowError()

        if (pos < 0 or pos >= self._count):
            raise IndexError()

        element: object = self._elements[pos]
        for i in range(pos, self._count - 1):
            self._elements[i] = self._elements[i + 1]
		
        self._count -= 1
        self._elements[self._count] = None
        return element

    def get(self, pos: int) -> object:
        if (pos < 0 or pos >= self._count):
            raise IndexError()
        return self._elements[pos]

    def search(self, element: object) -> int:
        for i in range(0, self._count):
            if (self._elements[i] == element):
                return i
        return -1
