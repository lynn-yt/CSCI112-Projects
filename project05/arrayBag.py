"""
Author: Sam Bluestone and Zahin Reaz
File: arrayBag.py
project04

Creates a bag with an array. 
"""
from arrays import Array
from abstractBag import AbstractBag

class ArrayBag(AbstractBag):
    """Interface for all bag types."""
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""

        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)
                
        

    # Accessor methods

    def __iter__(self):
        """Supports iteration over a view of self."""
        myModCount = self._modCount
        cursor = 0

        while cursor < len(self):
            yield self._items[cursor]
            if myModCount != self._modCount:
                raise AttributeError("Illegal modification of the backing store")
            cursor += 1


    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        super().resetSizeAndModCount()
        
    def add(self, item):
        """Adds item to self."""
        # resize here if needed
        if len(self._items) == self._size:
            self.grow()
            
        self._items[len(self)] = item
        self._size += 1
        super().incModCount()
        self._modCount = super().getModCount()
        
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
            super().incModCount()
            self._modCount = super().getModCount()
            
    def grow(self):
        """Doubles in size"""
        tempArray = Array(len(self._items) * 2)

        for i in range(self._size):
            tempArray[i] = self._items[i]

 

        self._items = tempArray


    
            
            
            
