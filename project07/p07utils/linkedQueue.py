"""
File: linkedQueue.py
Author: Sam Bluestone and Zahin Reaz
"""

from .node import Node
from .abstractCollection import AbstractCollection

class LinkedQueue(AbstractCollection):
    """A link-based queue implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front = self._rear = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        # Same as any linked iterator, except stacks
        cursor = self._front
        myModCount = self._modCount
        while cursor != self._rear.next:
            yield cursor.data
            if myModCount != self._modCount:
                raise AttributeError("Illegal modification of the backing store")
            cursor = cursor.next
        
        
    def peek(self):
        """
        Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("Cannot peek on empty queue")
        return self._front.data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        while not self.isEmpty():
            self.pop()

    def add(self, item):
        """Adds item to the rear of the queue."""
        newNode = Node(item)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode

        self._rear = newNode
        self._size += 1
        self.incModCount()

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("Cannot pop from an empty queue")
        else:
            data = self._front.data
            self._front = self._front.next
            self._size -= 1

        return data
            

            
        
        
