"""
Author: Sam Bluestone and Zahin Reaz
File: arrayBag.py

Speficitactions of the methods for all bag classes.  Running this code will
not produce any results, but it shows the headers and docstrings of the methods
that MUST be included or supported in any bag class.
"""
from arrays import Array
from arrayBag import ArrayBag

class ArraySortedBag(ArrayBag):
    """Interface for all bag types."""
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        super().__init__(sourceCollection)
                
        

    # Accessor methods


    def count(self, target):
        """Returns the number of a specific items in self."""
        index = self.binarySearch(target)
        if index == -1:
            return 0
        else:
            cnt = 1
            for x in range(index + 1, len(self)):
                if self._items[x] != target:
                    break
                cnt += 1
            for x in range(index - 1, -1, -1):
                if self._items[x] != target:
                    break
                cnt += 1
            
            return cnt


    def __contains__(self, target):
        left = 0
        right = len(self) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if target == self._items[midpoint]:
                return True
            elif target < self._items[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return False


    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        super().resetSizeAndModCount()
 
        
    def add(self, item):
        """Adds item to self."""
        # resize here if needed
        if len(self._items) == self._size:
            self.grow()

        if len(self) == 0:
            self._items[0] = item
            self._size += 1
        elif self._items[0] >= item:
            self.insert(item, 0)
        elif self._items[len(self) - 1] <= item:
            self.insert(item, len(self))
        else:
            for x in range(len(self) - 1):
                if self._items[x] <= item and self._items[x+1] >= item:
                    self.insert(item, x + 1)
                    break

        super().incModCount()
        self._modCount = super().getModCount()
                
    def insert(self, item, x):
        for j in range(len(self), x, -1):
            self._items[j] = self._items[j - 1]

        self._items[x] = item
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
            index = self.binarySearch(item)

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
        
    def binarySearch(self, target):
        left = 0
        right = len(self) - 1
        while left <= right:

            midpoint = (left + right) // 2
            if target == self._items[midpoint]:
                return midpoint
            elif target < self._items[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1

        return -1


            
            
            
