"""
File: expressionTree.py

Sam Bluestone and Zahin Reaz

Defines nodes for expression trees.
"""

from .tokens import Token
import math

class LeafNode(object):
    """Represents an integer."""

    def __init__(self, data):
        """Creates a leaf node with the given datum (an integer)."""
        self.data = data

    def value(self):
        """Returns the value of the expression."""
        # Exercise
        return self.data
      
    def prefix(self):
        """Returns the expression in prefix form."""
        # Exercise
        return str(self)

    def infix(self):
        """Returns the expression in infix form."""
        # Exercise
        return str(self)

    def postfix(self):
        """Returns the expression in postfix form."""
        return str(self)

    def __str__(self):
        """Returns the string rep of the expression."""
        return str(self.data)

class InteriorNode(object):
    """Represents an operator and its two operands."""

    def __init__(self, opToken, leftOper, rightOper):
        """Creates an interior node with the given operator (a token),
        and left and right operands (other nodes)."""
        self.operator = opToken
        self.leftOperand = leftOper
        self.rightOperand = rightOper

    def value(self):
        """Returns the value of the expression."""
        # Exercise
        if self.operator.getType() == Token.PLUS:
            return self.leftOperand.value() + self.rightOperand.value()
        if self.operator.getType() == Token.MINUS:
            return self.leftOperand.value() - self.rightOperand.value()
        if self.operator.getType() == Token.MUL:
            return self.leftOperand.value() * self.rightOperand.value()
        if self.operator.getType() == Token.DIV:
            return self.leftOperand.value() / self.rightOperand.value()
        if self.operator.getType() == Token.MOD:
            return self.leftOperand.value() % self.rightOperand.value()
        if self.operator.getType() == Token.EXP:
            return self.leftOperand.value() ** self.rightOperand.value()
        
        
      
    def prefix(self):
        """Returns the expression in prefix form."""
        # Exercise
        return str(self.operator) + " " + str(self.leftOperand.prefix()) + " " + str(self.rightOperand.prefix())
               

    def infix(self):
        """Returns the expression in infix form (fully parenthesized)."""
        # Exercise
        return "(" + str(self.leftOperand.infix()) + " " + str(self.operator) + " " + str(self.rightOperand.infix()) + ")" 

    def postfix(self):
        """Returns the expression in postfic form."""
        # Exercise
        return str(self.leftOperand.postfix()) + " " + str(self.rightOperand.postfix()) + " " + str(self.operator)

    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if type(node) == LeafNode:
                return ("| " * level) + str(node) + "\n"
            if node != None:
                s += recurse(node.rightOperand, level + 1)
                s += "| " * level
                s += str(node.operator) + "\n"
                s += recurse(node.leftOperand, level + 1)
            return s
        return recurse(self, 0)

def main():
    a = LeafNode(4)
    b = InteriorNode(Token('+'), LeafNode(2), LeafNode(3))
    c = InteriorNode(Token('*'), a, b)
    c = InteriorNode(Token('-'), c, b) 
    print("Expect ((4 * (2 + 3)) - (2 + 3)) :", c.infix())
    print("Expect - * 4 + 2 3 + 2 3         :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + -         :", c.postfix())
    print("Expect 15                        :", c.value())
    print(b)

if __name__ == "__main__":
    main()




