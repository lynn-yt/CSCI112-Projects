"""
Author: Sam Bluestone and Zahin Reaz
File: arraySortedSet.py
Description: Creates a set made from an array in sorted order
"""
from arraySortedBag import ArraySortedBag
from abstractSet import AbstractSet

class ArraySortedSet(ArraySortedBag, AbstractSet):
    """Interface for all set types."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        super().__init__(sourceCollection)

    # Accessor methods




    # Mutator methods


    def add(self, item):
        """Adds item to self."""
        if item not in self:
            super().add(item)
            super().incModCount()
            self._modCount = super().getModCount()
