"""
File: parsers.py
Sam Bluestone and Zahin Reaz

"""

from modules.tree.tokens import Token
from scanner import Scanner
from modules.tree.expressionTree import InteriorNode, LeafNode

class Parser(object):
    """Represents a parser for arithmetic expressions."""

    def parse(self, sourceStr):
        """Sets up and runs the parser on a source string."""
        self.completionMessage = "No errors"
        self.parseSuccessful = True
        self.scanner = Scanner(sourceStr)
        
        self.tree = self.expression()
        
        self.accept(self.scanner.get(), Token.EOE,
                    "symbol after end of expression")
    
   
    def parseStatus(self):
        """Returns the completion message for the parse."""
        self.completionMessage = "Value: " + str(self.tree.value())
        self.completionMessage += "\nPrefix: " + self.tree.prefix()
        self.completionMessage += "\nInfix: " + self.tree.infix()
        self.completionMessage += "\nPostfix: " + self.tree.postfix()
        return self.completionMessage
    
    def accept(self, token, expected, errorMessage):
        """Checks the type of the given token for correctness."""
        if token.getType() != expected:
            self.fatalError(token, errorMessage)

    def fatalError(self, token, errorMessage):
        """Stops the parse with a syntax error messahge."""
        self.parseSuccessful = False
        self.completionMessage = "Parsing error -- " + \
                                 errorMessage + \
                                 "\nExpression so far = " + \
                                 self.scanner.stringUpToCurrentToken()
        raise Exception(self.completionMessage)

    # expression = term { addingOperator term }
    def expression(self):
        self.tree = self.term()
        token = self.scanner.get()
        while token.getType() in (Token.PLUS, Token.MINUS):
            self.scanner.next()
            self.tree = InteriorNode(token, self.tree, self.term())
            token = self.scanner.get()

        return self.tree
        
            

    # term = factor { multiplyingOperator factor }
    def term(self):
        self.tree = self.factor()
        token = self.scanner.get()
        while token.getType() in (Token.MUL, Token.DIV, Token.MOD):
            self.scanner.next()
            self.tree = InteriorNode(token, self.tree, self.factor())
            token = self.scanner.get()

        return self.tree

    #factor = primary ["^" primary]
    def factor(self):
        self.tree = self.primary()
        token = self.scanner.get()
        if token.getType() == Token.EXP:
            self.scanner.next()
            self.tree = InteriorNode(token, self.tree, self.primary())
            
        return self.tree
            
        

    # primary = number | "(" expression ")"
    def primary(self):
        token = self.scanner.get()
        if token.getType() == Token.INT:
            self.tree = LeafNode(token.getValue())
            self.scanner.next()
        elif token.getType() == Token.L_PAR:
            self.scanner.next()
            self.tree = self.expression()
            self.accept(self.scanner.get(),
                        Token.R_PAR,
                        "')' expected")
            self.scanner.next()
        else:
            self.tree = LeafNode(token.getValue())
            self.fatalError(token, "bad primary")

        return self.tree


        




