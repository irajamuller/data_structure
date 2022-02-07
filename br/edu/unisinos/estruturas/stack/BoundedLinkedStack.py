from Exceptions import OverflowError
from UnboundedLinkedStack import UnboundedLinkedStack
from ADTStack import ADTStack

class BoundedLinkedStack(UnboundedLinkedStack):
    def __init__(self, size: int = ADTStack.DEFAULT_SIZE) -> None:
        super().__init__()
        self._size: int = size

    def is_full(self) -> bool:
        return len(self) == self._size

    def push(self, element: object) -> None:
        if self.is_full():
            raise OverflowError()
        super().push(element)