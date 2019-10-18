"""
Authors: Sam Bluestone, Zahin Reaz
project01
Filename: nQueens.py
Description: Contains two algorithims to solve the nQueens problem.
"""
import time


def nQueensFancy(n=8, counter = None):
   """Solves the n queens problem by back tracking and
      and only checking the queens behind it. If the queen cannot
      be placed safely, the program moves previous queens until the
      current queen can be placed safely"""
   board = [0 for x in range(n)]
   currentQueen = 0
   while True:
      if counter: counter.increment()

      if safeQueen(board, currentQueen, counter):
         currentQueen += 1
         if currentQueen == len(board):
            break
      else:
        
         while board[currentQueen] == len(board) - 1:
            if counter: counter.increment()
            board[currentQueen] = 0
            currentQueen -= 1

         board[currentQueen] += 1
               

   return board
   

   

def safeQueen(board, currentQueen, counter):
   """Checks the current queen's safety based on the queens to the
      left of it."""
   
   for colQ2 in range(currentQueen):
      if counter: counter.increment()
      if checkVertical(board[currentQueen], board[colQ2]) or \
         checkDiagonal(board[currentQueen], currentQueen, board[colQ2], colQ2):
         return False
         
   return True

def nQueensBrute(n=8, counter = None):
   # Set up the board with all the queens in row 0
   board = [0 for x in range(n)]
   
   # Continue to move queens until the board is safe
   while(not(safeBoard(board, counter))):
      if counter: counter.increment()
      # There's at least one overflow if we're in this loop, start with the first queen
      overflow = True
      currentQueen = len(board) - 1
      
      # While we need to move queens, move them and check for overflow
      while(overflow):
         if counter: counter.increment()
         board[currentQueen] += 1
         
         # If the queen we moved has fallen off the board, we overflow to the next queen
         if board[currentQueen] == len(board):
            board[currentQueen] = 0
            currentQueen -= 1
         
         # Otherwise we can stop moving queens
         else:
            overflow = False
            
   # We've hit the end, we can print a solution!
   return board


def printBoard(board):
   
   if board == None:
      return
   # Print the top border
   print("----" * len(board) + "-")
   
   # Iterate through the board and print Q if we have a queen there
   for row in range(len(board)):
      print("| ", end="")
      for col in range(len(board)):
         if board[col] == row:
            print("Q | ", end="")
         else:
            print("  | ", end="")
      
      # Print a line between the queens
      print()
      print("----" * len(board) + "-")
      

def safeBoard(board, counter):
   # Check all queens to be safe, return false if not safe
   
   for colQ1 in range(len(board)):
      if counter: counter.increment()
      for colQ2 in range(colQ1+1,len(board)):
         if counter: counter.increment()
         if checkVertical(board[colQ1], board[colQ2]) or checkDiagonal(board[colQ1], colQ1, board[colQ2], colQ2):
            return False
         
   return True



   
def checkVertical(rowQ1, rowQ2):
   # Return if two queens on horizontal
   return rowQ1 == rowQ2

def checkDiagonal(rowQ1, colQ1, rowQ2, colQ2):
   # return if two queens on diagonal
   diffRow = abs(rowQ1 - rowQ2)
   diffCol = abs(colQ1 - colQ2)
   
   return diffRow == diffCol
   

def main():
   
   number = int(input("Enter the size of the board: "))
   if number >= 4:
      
      start = time.time()
      bruteBoard = nQueensBrute(number)
      end = time.time()
      bruteElapsed = end - start
      
      start = time.time()
      fancyBoard = nQueensFancy(number)
      end = time.time()
      fancyElapsed = end - start
      
      
      print("N Queens brute force time elapsed: %.10f" % (bruteElapsed))
      print("N Queens fancy style time elapsed: %.10f" % (fancyElapsed))
      
      print("\nBrute Force")
      printBoard(bruteBoard)
      
      print("\nFancy")
      printBoard(fancyBoard)
      
      
   else:
      print("Number too small!")
   



if __name__ == '__main__':
   main()
