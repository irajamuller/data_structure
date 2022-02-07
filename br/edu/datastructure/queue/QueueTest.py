from UnboundedArrayQueue import UnboundedArrayQueue
from BoundedArrayQueue import BoundedArrayQueue
from CircularBoundedArrayQueue import CircularBoundedArrayQueue
from ADTQueue import ADTQueue
from UnboundedLinkedQueue import UnboundedLinkedQueue

if __name__ == "__main__":
    q: ADTQueue = UnboundedLinkedQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    print(f"size {len(q)}")
    print(q.dequeue())
    print(q)
    print(f"size {len(q)}")
    q.enqueue(6)
    print(q)
    print(f"size {len(q)}")
    for item in q:
        print(item)
    print(q.peek())
