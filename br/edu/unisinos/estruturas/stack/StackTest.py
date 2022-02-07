from BoundedLinkedStack import BoundedLinkedStack
from UnboundedLinkedStack import UnboundedLinkedStack
from BoundedArrayStack import BoundedArrayStack
from UnboundedArrayStack import UnboundedArrayStack
from IStack import IStack

if __name__ == "__main__":
    s: IStack = UnboundedArrayStack()
    for i in range(10):
        s.push(i)
    print(s)
    s.clear()
    print("peek %d" % (s.peek()))
    print("isEmpty %s" % (s.isEmpty()))
    print("isFull %s" % (s.isFull()))
    print("pop %d" % (s.pop()))
    print("len %d" % (s.size()))
    print(s)
    for item in s:
        print(item)
    s.push(9)
