"""
Authors: Sam Bluestone and Zahin Reaz
File name: abstractSet.py
Description: Creates methods to be applied to sets
that perform union, intersection, and difference operations
"""

class AbstractSet(object):

    def __or__(self, other):
        return self + other
           
            

    def __and__(self, other):
        result = type(self)()

        for item in self:
            if item in other:
                result.add(item)

        return result
    

    def __sub__(self, other):
        result = type(self)()
        for item in self:
            if not item in other:
                result.add(item)

        return result

