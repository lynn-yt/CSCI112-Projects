"""
File: abstractDict.py

Sam Bluestone and Zahin Reaz

Common data and method implementations for dictionaries.
"""
from ..abstractCollection import AbstractCollection

class AbstractDict(AbstractCollection):
    """Represents an abstract dictionary."""

    # Exercise
    def __init__(self, keys, values):
        """Initialize the collection."""
        super().__init__(None)
        
        if keys:
            valueIter = iter(values)
            for key in keys:
                self[key] = next(valueIter)

    def __str__(self):
        return " {" + ", ".join(map(lambda entry: str(entry.key) + \
               ": " + str(entry.value), self.entries())) + "}"

    def get(self, key, defaultValue = None):
        """Returns the associated value if the key is in the
        dictionary, or returns the default value otherwise."""
        if key in self:
            return key
        return defaultValue
   
    def add(self, entry):
        """Adds the values contained in an Entry parameter to the current dictionary."""
        self[entry.key] = entry

        
    # Exercise
    def keys(self):
        """Returns an iterator on the keys in the dictionary."""
        return iter(self)   

    # Exercise
    def values(self):
        """Returns an iterator on the values in the dictionary."""
        lyst = []
        for key in self:
            lyst.append(self[key])
        return iter(lyst)

    # Exercise
    def entries(self):
        """Returns a iterator on the entries in the dictionary."""
        lyst = []
        for key in self:
            lyst.append(self._getEntry(key))

        return iter(lyst)
                    

    # Exercise
    def __add__(self, other):
        """Returns a dictionary containing the entries of self and
        otherDict.  When keys are equal, the value in otherDict replaces
        the value in self."""

        if self.keys() == other.keys():
            return type(other)(other.keys(), other.values())

        keys = []
        for key in self.keys():
            keys.append(key)

        for key in other.keys():
            keys.append(key)

        values = []
        for value in self.values():
            values.append(value)

        for value in other.values():
            values.append(value)

        return type(self)(iter(keys), iter(values))
        

    # Exercise
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or  \
           len(self) != len(other):
            return False
        for key in self:
            if not key in other:
                return False

        return True
       


    def _getEntry(self, key):
        """Helper method to obtain the entry rather than the value associated with a key."""
        raise NotImplementedError("Abstract class method invoked!")
    
class Entry(object):
    """Represents a dictionary entry.  Supports comparisons by key."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other): return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other): return False
        return self.key <= other.key

    def __hash__(self):
        return hash(self.key)
