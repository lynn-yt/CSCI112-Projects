from p07utils.linkedStack import LinkedStack
from p07utils.arrayQueue import ArrayQueue
from p07utils.grid import Grid


def getMazeFromFile():
    name = input("Enter name of maze: ")
    fileObj = open(name, "r")

    firstLine = list(map(int, fileObj.readline().strip().split()))
    rows = firstLine[0]
    cols = firstLine[1]

    maze = Grid(rows, cols, "*")
    
    for row in range(rows):
        line = fileObj.readline().strip()

        col = 0
        for ch in line:
            maze[row][col] = ch
            col += 1
    
    fileObj.close()
    
    return maze

def findStartPos(maze):
    for row in range(maze.getHeight()):
        for col in range(maze.getWidth()):
            if maze[row][col] == "S":
                return(row, col)

    return(-1, -1)

def getOut(startRow, startCol, maze, showProcess=False, choiceStorage = LinkedStack):

    choices = choiceStorage()
    choices.add((startRow, startCol))

    while not choices.isEmpty():
        c = choices.pop()
        if maze[c[0]][c[1]] == "G":
            return True
        else:
            maze[c[0]][c[1]] = "."

            if showProcess:
                print(maze)
                if input("Press enter to continue, q to skip to the end: ") == "q":
                    showProcess = False

            for newRow, newCol in [(c[0]+1, c[1]),
                                   (c[0]-1, c[1]),
                                   (c[0], c[1]+1),
                                   (c[0], c[1]-1)]:
                if newRow >= 0 and newRow < maze.getHeight() and \
                   newCol >= 0 and newCol < maze.getWidth() and \
                   maze[newRow][newCol] not in ".*":
                    choices.add((newRow, newCol))
    
    return False


def main():
    maze = getMazeFromFile()
    print(maze)
    
    (startRow, startCol) = findStartPos(maze)

    success = getOut(startRow, startCol, maze, True, choiceStorage = ArrayQueue)
    #success = getOut(startRow, startCol, maze)

    if success:
        print("Maze solved!")
        print(maze)
    else:
        print("No way out of this maze.")


if __name__ == "__main__":
    main()
