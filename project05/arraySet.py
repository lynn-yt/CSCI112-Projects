"""
Author: Sam Bluestone and Zahin Reaz
File: ararySet.py
Description: Creates a set that utilizes an array to store information
"""
from arrayBag import ArrayBag
from abstractSet import AbstractSet

class ArraySet(ArrayBag, AbstractSet):
    """Interface for all set types."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        super().__init__(sourceCollection)

    # Accessor methods



    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False

        for item in self:
            if not item in other:
                return False

        return True

    
    # Set-specific methods


    # Mutator methods
  

    def add(self, item):
        """Adds item to self."""
        if item not in self:
            super().add(item)
            super().incModCount()
            self._modCount = super().getModCount()

 
