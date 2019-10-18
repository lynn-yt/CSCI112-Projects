"""
Author: Sam Bluestone and Zahin Reaz
File: arrayBag.py
project04

Creates a bag with an array. 
"""
from arrays import Array

class ArrayBag(object):
    """Interface for all bag types."""
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._size = 0
        self._modCount = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)

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
        """Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        myModCount = self._modCount
        cursor = 0

        while cursor < len(self):
            yield self._items[cursor]
            if myModCount != self._modCount:
                raise AttributeError("Cannot modify!")
            cursor += 1
            
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
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._modCount += 1
        
    def add(self, item):
        """Adds item to self."""
        # resize here if needed
        if len(self._items) == self._size:
            self.grow()
            
        self._items[len(self)] = item
        self._size += 1
        self._modCount += 1
        
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in bag")
        else:
            #find the index of the item
            for index in range(len(self)):
                if self._items[index] == item:
                    break

            #remove the item and shift elements
            for j in range(index, self._size - 1):
                self._items[j] = self._items[j + 1]

            self._size -= 1
    def grow(self):
        """Doubles in size"""
        tempArray = Array(len(self._items) * 2)

        for i in range(self._size):
            tempArray[i] = self._items[i]

 

        self._items = tempArray

            
            
            
