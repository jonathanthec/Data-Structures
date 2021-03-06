from doubly_linked_list.doubly_linked_list import DoublyLinkedList
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
"""


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def len(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_from_head()
