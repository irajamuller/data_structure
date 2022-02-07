class Node:
    def __init__(self, element: object) -> None:
        self.element = element
        self.next: Node = None
    
    def __str__(self) -> str:
        return str(self.element)

class DNode(Node):
    def __init__(self, element: object) -> None:
        super().__init__(element)
        self.prev: Node = None
