#Pancake example - can only put on top and take it off the top

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
      - Stack is applies in both Statis implementation (Arrays) and Dynamic implementation (Linked Lists)

"""
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
       # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.value = value

        self.storage.add_to_head(value)
        self.size += 1


    def __len__(self):
        return self.size

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()


    

