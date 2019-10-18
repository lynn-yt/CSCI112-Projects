"""
File name: lineWrap.py
Authors: Sam Bluestone and Zahin Reaz
Description: Reads a file specified by the user and writes to
a new file the same string line wrapped to a user-specified
number of characters
"""
from arrayList import ArrayList

def main():
    fileName = input("Enter a file name: ")
    fileObj = open(fileName, "r")
    text = fileObj.read()
    fileObj.close()
    characters = int(input("Enter the number of characters to linewrap to: "))
    lineWrap(text, characters, fileName)


def lineWrap(text, characters, fileName):
    """Using an ArrayList of words in the file, wraps the text
        based on the number of characters specified by the user"""

    #copies the words into the ArrayList
    words = text.split(" ")
    wordsList = ArrayList(words)

    #wraps the text into a string variable
    string = ""
    charactersInLine = 0
    for word in wordsList:
        if len(word) > characters:
            raise Exception("Word in file: \"" + word + "\" " + " has more characters than the number of characters to linewrap to.")
        if charactersInLine + len(word) < characters:
            string += word + " "
            charactersInLine += len(word)
        else:
            string += "\n" + word + " "
            charactersInLine = len(word)    
    
    #writes the new string to an appropriately named file
    file = open("wrap_" + fileName, 'w')
    file.write(string)
    file.close()



if __name__ == "__main__":
    main()
        
    
    
