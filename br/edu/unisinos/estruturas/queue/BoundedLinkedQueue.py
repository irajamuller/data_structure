from ADTQueue import ADTQueue
from Node import Node
from UnboundedLinkedQueue import UnboundedArrayQueue

class BoundedArrayQueue(UnboundedArrayQueue):
    def __init__(self, size: int = ADTQueue.DEFAULT_SIZE) -> None:
        super().__init__()
        self._size: int = size

    def is_full(self) -> bool:
        return len(self) == self._size

    def enqueue(self, element: object) -> None:
        if self.is_full():
            raise OverflowError()
        super().enqueue(element)