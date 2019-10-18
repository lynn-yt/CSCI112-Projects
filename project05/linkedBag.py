"""
Author: Sam Bluestone, Zahin Reaz
File: linkedBag.py

Speficitactions of the methods for all bag classes.  Running this code will
not produce any results, but it shows the headers and docstrings of the methods
that MUST be included or supported in any bag class.
"""
from node import Node
from abstractBag import AbstractBag

class LinkedBag(AbstractBag):
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""

        self._items = None
        super().__init__(sourceCollection)

    # Accessor methods




    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items
        myModCount = self._modCount
        while cursor != None:
            yield cursor.data
            if myModCount != self._modCount:
                raise AttributeError("Illegal modification of the backing store")
            cursor = cursor.next

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._items = None
        super().resetSizeAndModCount()


    def add(self, item):
        """Adds item to self."""
        self._items = Node(item, self._items)
        self._size += 1
        super().incModCount()
        self._modCount = super().getModCount()
        
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if item not in self:
            raise KeyError("Item not in bag")
        else:
            if len(self) == 1 or self._items.data == item:
                self._items = self._items.next

            else:
                probe = self._items
                while probe.next != None and probe.next.data != item:
                    probe = probe.next
                
                probe.next = probe.next.next
            self._size -= 1
            super().incModCount()
            self._modCount = super().getModCount()
                
                
                
