"""
File: hashDict.py

Sam Bluestone and Zahin Reaz

A hash-based dictionary.
"""

from .abstractDict import AbstractDict, Entry
from ..node import Node
from ..arrays import Array

class HashDict(AbstractDict):
    """Represents a hash-based dictionary."""

    DEFAULT_CAPACITY = 10
    MAX_LOAD_FACTOR = 0.5
    MIN_LOAD_FACTOR = 0.1

    def __init__(self, sourceKeys = None, sourceValues = None,
                 capacity = DEFAULT_CAPACITY):
        """Sets the initial state of self, which includes the
        contents of  source keys and source values, if they
        are present."""
        self._array = Array(capacity)
        self._foundEntry = self._priorEntry = None
        self._index = -1
        super().__init__(sourceKeys, sourceValues)

    # Exercise
    def __iter__(self):
        """Serves up the keys in the dictionary."""
        lyst = []
        for bucket in self._array:
            node = bucket
            while node != None:
                lyst.append(node.data.key)
                node = node.next

        return iter(lyst)

    # Exercise
    def __getitem__(self, key):
        """Precondition: the key is in the dictionary. Resizes
        when load factor is > MAX_LOAD_FACTOR
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""        
        
        if key not in self:
            raise KeyError("Key is not in the dictionary.")
        if self.loadFactor() > HashDict.MAX_LOAD_FACTOR:
            self._rehash(2)

        return self._foundEntry.data.value
        
    
    # Exercise
    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it.
        Othwerise, replaces the old value with the new
        value."""
        
        if key not in self:
            newEntry = (Node(Entry(key, value), self._array[self._index]))
            self._array[self._index] = newEntry
            self._size += 1
            self.incModCount()
            if self.loadFactor() > HashDict.MAX_LOAD_FACTOR:
                self._rehash(2) 
        else:
            self._array[self._index].data.value = value
            
        
    def _rehash(self, resizeFactor):
        """Rehashes the current values into an array twice the size.
        resizeFactor is a float by which to increase or decrease the
        array size (2 means to double, 0.5 means to halve).
        Will only shrink if the new size is not less than the default
        capacity."""
        if len(self._array) * resizeFactor >= HashDict.DEFAULT_CAPACITY:
            oldArray = self._array
            self._array = Array(int(len(self._array) * resizeFactor))
            self._size = 0
            for bucket in oldArray:
                cursor = bucket
                while cursor != None:
                    self[cursor.data.key] = cursor.data.value
                    cursor = cursor.next
       
        
    
    def _getEntry(self, key):
        """Helper method to obtain the entry rather than the value associated with a key."""
        if key in self:
            return self._foundEntry.data
        return None
        
    
    def loadFactor(self):
        """Returns the load factor of the current hash size."""
        return self._size / len(self._array)

    # Exercise
    def pop(self, key, defaultValue = None):
        """Removes the key and returns the associated value if the
        key in in the dictionary, or returns the default value
        otherwise. Resizes when load factor is < MIN_LOAD_FACTOR"""
        if key not in self:
            return defaultValue

        data = self._foundEntry.data.value
        
        if self._priorEntry == None:
            self._array[self._index] = self._foundEntry.next
        else:
            self._priorEntry.next = self._foundEntry.next

        self._size -= 1
        
        if self.loadFactor() < HashDict.MIN_LOAD_FACTOR:
            self._rehash(.5)
            
        return data
        
        

    def clear(self):
        """Makes self become empty."""
        self.resetSizeAndModCount()
        self._array = Array(HashDict.DEFAULT_CAPACITY)
        self._foundEntry = self._priorEntry = None
        self._index = -1

    # Exercise
    def __contains__(self, key):
        """Returns True if the key in in the dictionary
        or False otherwise."""
        
        self._index = abs(hash(key)) % len(self._array)
        self._priorEntry = None
        self._foundEntry = self._array[self._index]
        while self._foundEntry != None:
            if self._foundEntry.data.key == key:
                return True
            else:
                self._priorEntry = self._foundEntry
                self._foundEntry = self._foundEntry.next
        return False



                
