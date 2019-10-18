"""
Authors: Sam Bluestone and Zahin Reaz
project04
File name: miniScrabble.py
Description: Plays a fragmented Scrabbled game using an ArraySortedBag
"""


from arraySortedBag import ArraySortedBag
import random
from arraySet import ArraySet


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
        self.player1Words = ArraySet()
        self.player2Words = ArraySet()
        self.turn = 0
        
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
        bag = ArraySortedBag(self.letters)
        score = 0
        if self.turn % 2 == 1:
            if word in self.player1Words:#returns -2 if the word has already been made by the other player
                return -2
            elif word in self.player2Words: #returns -3 if the player has already made the word
                return -3
            else:
                self.player2Words.add(word)

        else:
            if word in self.player2Words:
                return -2
            elif word in self.player1Words:
                return -3
            else:
                self.player1Words.add(word)

        score = self.scoreWord(word)
        for letter in word:
            if letter in bag:
                bag.remove(letter)
            elif self.turn % 2 == 0:
                self.player1Words.remove(word)
                return -1
            else:
                self.player2Words.remove(word)
                return -1 

               
        return score


    def scoreWord(self, word):
        """Returns the score of a given word """
        score = 0
        for letter in word:
            score += self.dic[letter]

        return score


    def scorePlayer(self, words):
        """Returns the score of a given player's words"""
        score = 0
        for word in words:
            score += self.scoreWord(word)
        return score
        
def main():
    game = MiniScrabble()

    while True:
        print('Available letters: ' + str(game.letters))
        word = input('Player ' + str(game.turn % 2 + 1) + '>')
        score = game.checkWord(word)
   
        if score == -1:
            print("You can't make that word with those letters, you lose!")
            print("You found the following words:")
            print("Player One: " + str(game.player1Words) + ", Score: " + str(game.scorePlayer(game.player1Words)))
            print("Player Two: " + str(game.player2Words) + ", Score: " + str(game.scorePlayer(game.player2Words)))
            break
        elif score == -2:
            print("The other player used that word! Game over!")
            print("You found the following words:")
            print("Player One: " + str(game.player1Words) + ", Score: " + str(game.scorePlayer(game.player1Words)))
            print("Player Two: " + str(game.player2Words) + ", Score: " + str(game.scorePlayer(game.player2Words)))
            break
        else:
            if score != -3:
                print("You scored " + str(score) + " points!\n\n")
            game.turn += 1

if __name__ == "__main__":
    main()
    
            
        

