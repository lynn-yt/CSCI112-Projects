"""
Author: Sam Bluestone, Zahin Reaz
project04
File: linkedBag.py
Description: Creates a Linked Bag structure

"""
from node import Node

class LinkedBag(object):
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._size = 0
        self._modCount = 0
        self._items = None

        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def count(self, target):
        """Returns the number of a specific items in self."""
        cnt = 0
        for item in self:
            if item == target:
                cnt += 1

        return cnt    
    def __len__(self):
        """-Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items

        while cursor != None:
            yield cursor.data
            cursor = cursor.next
 
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = type(self)(self)

        for item in other:
            result.add(item)

        return result
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True

        if type(self) != type(other): return False

        if len(self) != len(other): return False

        for item in self:
            if self.count(item) != other.count(item):
                return False

        return True
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = None        

    def add(self, item):
        """Adds item to self."""
        self._items = Node(item, self._items)
        self._size += 1
        
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
                
                
                
