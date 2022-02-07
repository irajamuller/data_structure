from BoundedLinkedStack import BoundedLinkedStack
from UnboundedLinkedStack import UnboundedLinkedStack
from BoundedArrayStack import BoundedArrayStack
from UnboundedArrayStack import UnboundedArrayStack
from ADTStack import ADTStack

if __name__ == "__main__":
    s: ADTStack = UnboundedLinkedStack()
    for i in range(10):
        s.push(i)
    print(s)
    print("peek %d" % (s.peek()))
    print("isEmpty %s" % (s.is_empty()))
    print("isFull %s" % (s.is_full()))
    print("pop %d" % (s.pop()))
    print("len %d" % (s.size()))
    print(s)
    for item in s:
        print(item)
    s.push(9)
