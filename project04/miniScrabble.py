"""
Authors: Sam Bluestone and Zahin Reaz
project04
File name: miniScrabble.py
Description: Plays a fragmented Scrabbled game using an ArraySortedBag
"""


from arraySortedBag import ArraySortedBag
import random



class MiniScrabble(object):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    def __init__(self):
        """Constructor initializes a sorted ArrayBag and populates it
            with letters. Creates a dictionary to contain the scores of
            each letter"""

        self.letters = ArraySortedBag()
        self.generate()
        self.dic = {}
        for key in ['e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u']:
            self.dic[key] = 1
        for key in ['d', 'g']:
            self.dic[key] = 2
        for key in ['b', 'c', 'm', 'p']:
            self.dic[key] = 3
        for key in ['f', 'h', 'v', 'w', 'y']:
            self.dic[key] = 4
        self.dic['k'] = 5
        for key in ['j', 'x']:
            self.dic[key] = 8
        for key in ['q', 'z']:
            self.dic[key] = 10

    def generate(self, v = 10, c = 15):
        """Randomly generates a given number of vowels and consanants.
            Default is 10 vowels and 15 consonants"""
        self.letters.clear()
        for x in range(v):
            self.letters.add(MiniScrabble.VOWELS[random.randint(0, len(MiniScrabble.VOWELS) - 1)])
        for x in range(c):
            self.letters.add(MiniScrabble.CONSONANTS[random.randint(0, len(MiniScrabble.CONSONANTS) - 1)])

    def checkWord(self, word):
        """Checks if a word is valid and if it is, the score is returned
            and if it is not a valid word, -1 is returned"""
        score = 0
        for letter in word:
            if letter in self.letters:
                score += self.dic[letter]
                self.letters.remove(letter)
            else:
                return -1
            
        return score



def main():
    game = MiniScrabble()

    while True:
        print('Available letters: ' + str(game.letters))
        word = input('Make a word> ')
        score = game.checkWord(word)
        if score == -1:
            print("You can't make that word with those letters, you lose!")
            break
        else:
            print("You scored " + str(score) + " points!\n\n")

if __name__ == "__main__":
    main()
    
            
        

