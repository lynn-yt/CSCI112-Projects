"""
Authors: Sam Bluestone, Zahin Reaz
FileName: arrayList.py
project03
Description: Implements an ArrayList object that contains
an internal Array object and behaves like a normal python
list.
"""
from arrays import Array

import random

class ArrayList(object):
    """Simulates a List object using an Array"""
    
    def __init__(self, capacity = 10, fillValue = None):
        """Creates an internal Array to store items of the capacity.
             Should also create any other instance variables here."""
        self.logicalSize = 0
        self.initalCapacity = capacity
        self.defaultFill = fillValue
        self._items = Array(capacity, fillValue)

    def __len__(self):
        """Returns the capacity of the ArrayList"""
        return len(self._items)

    def __str__(self):
        """Returns a string representation of the ArrayList of the format
           [a, b, c, ... , z]
           Does not show any empty items."""
        if self.size() == 0:
            return '[]'
        
        retStr = '['
        for x in range(self.size() - 1):
            retStr += str(self[x]) + ', '

        retStr += str(self[self.size() - 1]) + ']'

        return retStr 
            

    def __iter__(self):
        """Returns default iterator. Must set up an instance variable
             to keep track of the current iteration place."""
        cursor = 0

        while cursor < self.size():
            yield self._items[cursor]
            cursor += 1


    def __getitem__(self, index):
        """Gets an item from a given index or
            gets a slice of items."""
        if type(index) == slice:

            start, end, step = index.indices(self.size())
            values = ArrayList(end - start)
            
            for x in range(start, end, step):
                values.append(self[x])
            return values
        
        if index >= 0 and index <= self.size():
            return self._items[index]
        else:
            raise Exception("Index must be greater than or equal to 0 and \
                            less than or equal to size()")

    def __setitem__(self, index, newItem):
        """Sets an item at a given index """
        if index >= 0 and index <= self.size():
            self._items[index] = newItem
        else:
            raise Exception("Index must be greater than or equal to 0 and \
                            less than or equal to size()")
        
    def __eq__(self, other):
        """Returns true if the other is an ArrayList and has the same
             contents as self."""
        if self is other: return True
        
        if type(self) != type(other) or self.size() != other.size():
            return False
        
        for item in self:
            if not item in other:
                return False

        for item in other:
            if not item in self:
                return False

        return True

        
    def size(self):
        """Returns the number of actual items in the array."""
        return self.logicalSize

    def grow(self):
        """Doubles in size"""
        tempArray = Array(len(self) * 2)

        for i in range(self.size()):
            tempArray[i] = self[i]

        for i in range(self.size() + 1, len(tempArray)):
            tempArray[i] = self.defaultFill

        self._items = tempArray
        

    def shrink(self):
        """Becomes half the current size, does not become smaller than
             initial capacity."""
        if len(self) // 2 > self.initialCapacity:
            tempArray = Array(len(self) // 2)

            for i in range(self.size()):
                tempArray[i] = self[i]

            self._items = tempArray
        else:
            raise Exception("Cannot shrink the ArrayList below the intialCapacity")

    def insert(self, index, newItem):
        """Inserts a new item at the provided index. Resizes if the
             number of items in the ArrayList equals its current
             capacity."""
        if self.size() == len(self):
            self.grow()

        for j in range(self.size(), index, -1):
            self[j] = self[j - 1]


        self[index] = newItem
        self.logicalSize += 1

        

    def pop(self, index):
        """Pops the item at the provided index. Resizes if the number
             of items in the ArrayList equals one fourth its current
             capacity."""
        value = self[index]
        for j in range(index, self.size()):
            self[j] = self[j + 1]

        self.logicalSize -= 1
        
        if self.size() // 4 == len(self):
            self.shrink()

        return value

    def append(self, newItem):
        """Appends an item to the end of the array. Resizes if the number
             of items in the ArrayList equals its current capacity."""
        if self.size() == len(self):
            self.grow()            

        self[self.size()] = newItem
        self.logicalSize += 1


def testArrayList():
    """Tests the functionality of the ArrayList class"""

    AL1 = ArrayList()
    AL2 = ArrayList(25)


    print("Capacity of AL1:", len(AL1))
    print("Size of AL1:", AL1.size())

    print("Capacity of AL2:", len(AL2))
    print("Size of AL2:", AL2.size())


    print("\nPutting 30 random numbers into AL1")

    for i in range(30):
        AL1.insert(i, random.randint(1,10))
       

    print("\nCapacity of AL1:", len(AL1))
    print("Size of AL1:", AL1.size())

    print("AL1 equal to AL2:", AL1 == AL2)

    print("\nCopying contents into AL2")
    for i in range(30):
        AL2.insert(i, AL1[i])
       

    print("\nAL1 equal to AL2:", AL1 == AL2)

    print(AL1)
    print(AL2)

    print("\nIterator test:")

    for i in AL1:
        print(i, end=" ")

    print('\n\nSlice test:')
    print(AL1[3:6])


    print("\n\nRemoving 30 items randomly from AL1")
    for i in range(29,-1,-1):
        AL1.pop(i)
       

    print(AL1)


    


if __name__ == "__main__":
    testArrayList()
    

    
