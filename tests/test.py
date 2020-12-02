#!/usr/bin/env python3

"""	node.data
	node.next
"""
from LinkedList import SinglyLinkedList
ll = SinglyLinkedList()
ll.add(1)
ll.add(2,0) #add(data,pos=None)
ll.add(3) 
ll.remove(2) #removes node with particular data
ll.pop()  #remove and returns element at particular position from the linkedlist or by default last element
ll.len() #returns length of the linkedlist
ll.getNode(1) #returns node of the first occurance with given data
print(ll) #prints the linkedlist
