from Exceptions import OverflowError
from UnboundedArrayQueue import UnboundedArrayQueue
from ADTQueue import ADTQueue

class BoundedArrayQueue(UnboundedArrayQueue):
    def __init__(self, size: int = ADTQueue.DEFAULT_SIZE) -> None:
        super().__init__(size)

    def is_full(self) -> bool:
        return len(self) == len(self._elements)

    def enqueue(self, element: object) -> None:
        if self.is_full():
            raise OverflowError()
        super().enqueue(element)