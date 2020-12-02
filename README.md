In this project we want to contribute a module called data_structures to the python programming language. We got inspiration from Java and thought that it would be useful if we include in python.
Generally when we want to implement some data structures like LinkedList, BST in Python, we have to do it from scratch like declaring class, methods, objects etc. This would be somewhat burden for everyone which takes so much time.
Not only these, in Python we have only one type of Set, which is unordered distinct collection of elements but if we a the situation where we want to preserve  insertion order of elements and suppose if we want sorted order of set elements then we have to implement from scratch which is again time taking and in-efficient.
So we want to implement a built in classes for such type of data strucures. So anyone who wishes to use them can easily by importing them .
Inset:- In this set elements are unique but the elements will be stored in the order in which they are inserted. Lets say we add alphabets 'a'....'z' when we want to retreive them we will get in the insertion order.
TreeSet:- And coming to next set which is Tree set here we store elements in sorted order. So when we want to search we can search them in O(logn) time using Binary search.
Single LinkedList:- Here data memebers are represented as nodes which are connected through refrence 					   variables. Every node contains two nodes one is data and another one is refrence to another node. In this LL only forward traversal is possible.
Doouble Linked List:- Here data memebers are represented as nodes which are connected through 							   refrence variables. Every node contains three nodes one is data and another two are refrences to previous node and next node respectively. In this LL only both forward and backward are possible.

from DataStructures.LinkedList.SinglyLinkedList import *

#Representation of node	

node.data

node.next
ll = SinglyLinkedList()

ll.add(1)

ll.add(2,0) #add(data,pos=None) it adds particular node at pos=0.

ll.add(3)  #it appends node to linkedlist by default.

ll.remove(2) #removes node with particular data

ll.pop()  #remove and returns node at particular position from the linkedlist or by default last element

ll.len() #returns length of the linkedlist

ll.getNode(1) #returns reference of the first occurance of node with given data.


print(ll) #prints the linkedlist


DataStructures/  			#Package
	__init__.py
	LinkedList/			#Sub-Packages
		__init__.py			
		SinglyLinkedList.py
		DoublyLinkedList.py
	Set/				#Sub-Packages
		__init__.py
		Inset.py
		TreeSet.py
	
	

from DataStructures.Set import Inset
sll = DataStructures.Set.SinglyLinkedList
sll = SinglyLinkedList()
s = Inset()


	




