from LinkedList import DoublyLinkedList


dll = DoublyLinkedList([i for i in range(1,7)])
print(dll)
dll.add(7)
dll.add(9,1)
print(dll)
dll.remove(9)
a = dll.getNode(6)
print(a.data)
print(dll.len())
print(dll)