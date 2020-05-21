#standing in line

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
    - Queue is applies in both Statis implementation (Arrays) and Dynamic implementation (Linked Lists)

   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.value = value
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -+ 1
            return self.storage.remove_from_tail()
        else:
            return None
