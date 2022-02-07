import numpy as np
from ADTList import ADTList
from UnboundedArrayList import UnboundedArrayList
from SinglyLinkedList import SinglyLinkedList
from DoublyLinkedList import DoublyLinkedList

if __name__ == "__main__":
    lista: ADTList = DoublyLinkedList()
    print(lista)
    for i in range(5, 0, -1):
        lista.insert_last(i)
    print(lista)
    print(lista.search(3))
    lista.insert(0, 2)
    print(lista)
    lista.remove(2)
    print(lista)
    lista.remove_first()
    print(lista)
    lista.remove_last()
    print(lista)
    print("size ", lista.size())
    print("empty ", lista.is_empty())    
    print("full ", lista.is_full())
    for i in lista:
        print(i)
