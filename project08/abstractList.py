"""
File: abstractlist.py
Author: Sam Bluestone and Zahin Reaz

Common data and method implementations for lists.
"""

from abstractCollection import AbstractCollection

class AbstractList(AbstractCollection):
    """Represents an abstract list."""

    def __init__(self, sourceCollection):
        """Sets up the collection."""
        super().__init__(sourceCollection)

    def index(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        
        if item not in self:
            raise ValueError("Item not in list.")
        else:
            index = 0
            while True:
                if self[index] == item:
                    return index
                else:
                    index += 1
                    
        
    
    def remove(self, item):
        """Precondition: item is in the list.
        Raises: ValueError if item in not in self.
        Postcondition: item is removed from self."""
        if item not in self:
            raise ValueError("Item not in list.")
        else:
            position = self.index(item)
            self.pop(position)
            
        

    def add(self, item):
        """Adds the item to the end of the list."""
        self.insert(len(self), item)
        

    def append(self, item):
        """Adds the item to the end of the list."""
        self.add(item)

    def listIterator(self):
        """Returns a list iterator, should not be invoked at this level."""
        raise NotImplementedError("Abstract class method invoked.")
