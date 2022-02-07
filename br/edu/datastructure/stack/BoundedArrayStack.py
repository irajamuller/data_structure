import numpy as np
from Exceptions import OverflowError
from UnboundedArrayStack import UnboundedArrayStack
from ADTStack import ADTStack

class BoundedArrayStack(UnboundedArrayStack):
    def __init__(self, size: int = ADTStack.DEFAULT_SIZE) -> None:
        super().__init__(size)

    def is_full(self) -> bool:
        return len(self) == len(self._elements)

    def push(self, element: object) -> None:
        if self.is_full():
            raise OverflowError()
        super().push(element)