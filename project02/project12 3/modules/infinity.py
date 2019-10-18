"""
infinity.py
Sam Bluestone and Zahin Reaz
"""

INFINITY = "-"



def addWithInfinity(a, b):
   """Adds a and b, with the possibility that either might be infinity."""
   if a== INFINITY or b == INFINITY:
      return INFINITY
   return a + b
    
def minWithInfinity(a, b):
   """Finds the minimum of a and b, with the possibility that either might be infinity."""
   if a == INFINITY and b == INFINITY:
      return INFINITY
   if lessThanWithInfinity(a, b):
      return a
   return b
   

def lessThanWithInfinity(a, b):
   """Returns a < b, with the possibility that either might be infinity."""
   if a == INFINITY:
      return False
   if b == INFINITY:
      return True
   return a < b
   
