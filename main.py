import random
import os
from words import word_list


lv = []
position_of_char = []

def read_lists_from_file(filename):
    with open(filename, "r") as file:
         for line in file:
            line_list = line.strip().split(", ")
            lv.append(line_list)
    return lv

read_lists_from_file("draw.txt")

class Hangman:
    def __init__(self, level):
        self.level = level
        self.word = self.get_word()
        self.word_length = len(self.word)
        
    def get_word(self):
        word = random.choice(word_list)
        return word.upper()

    def print_level(self, level):
            for item in level:
                print(item)

    def hidden_word(self):
         uline_word = "_ " * self.word_length
         return uline_word

def clear():
    os.system('cls')

def update_ul_word(ch):
    word = game.hidden_word().replace("_", ch)
    return word


game = Hangman(1)
result = ""
ul_word = game.hidden_word()

while game.level < 9:
    clear()
    print("Välkommen till Hangman!\n")

    for item in lv[game.level - 1]:
        print(item)
          
    # print(game.hidden_word())
    print(ul_word)

    print(game.word)
    print("\n")

    if result != "":
        print(result)

    if game.level == 8:
        print("GAME OVER!!!!\n")
        break
    else:
        guess = input("Gissa en bokstav: ").upper()
        if guess in game.word:
            result = "Rätt bokstav"
            
            ul_word = update_ul_word(guess)

            # for i, ch in ul_word:
            #     if ch == guess:
            #         position_of_char.append(i)

            # for ch in position_of_char:


        else:
            result = "Fel bokstav"
            game.level += 1

        