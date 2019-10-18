"""
Authors: Sam Bluestone and Zahin Reaz
File name: abstractBag.py
Description: Inherits from AbstractCollection and
creates a collection specific to a bag
"""
from abstractCollection import AbstractCollection

class AbstractBag(AbstractCollection):


    def __init__(self, sourceCollection = None):
        """Constructor uses AbstractCollection constructor """

        super().__init__(sourceCollection)

    def __eq__(self, other):
        """Overrides the __eq__ method to accurately test equality
            of two bags"""

        if self is other: return True

        if type(self) != type(other): return False

        if len(self) != len(other): return False

        for item in self:
            if self.count(item) != other.count(item):
                return False

        return True


    def count(self, target):
        """Returns the number of a specific items in self."""
        cnt = 0
        for item in self:
            if item == target:
                cnt += 1

        return cnt



    
        
