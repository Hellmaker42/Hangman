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
        cor_word_list = []
        for ch in word:
            cor_word_list.append(ch.upper())
        return cor_word_list

    def print_level(self, level):
            for item in level:
                print(item)

    def hidden_word(self):
         uline_word = "_" * len(correct_word_list)
         uline_word_list = []
         for ch in uline_word:
             uline_word_list.append(ch)
         return uline_word_list

def clear():
    os.system('cls')




game = Hangman(1)
result = ""
guessed_letter = []
correct_word_list = game.get_word()
ul_word_list = game.hidden_word()

while game.level < 9:
    clear()
    print("Välkommen till Hangman!")
    print("Kategorin är länder i Europa\n")

    for item in lv[game.level - 1]:
        print(item)
          
    # print(game.hidden_word())
    for ch in ul_word_list:
        print(ch + " ", end="")

    # print("\n")
    print(correct_word_list)
    print("\n")

    if result != "":
        print(result)

    if game.level == 8:
        print("GAME OVER!!!!\n")
        break
    elif "_" not in ul_word_list:
        print("Grattis du klarde dig levande.")    
        break  
    else:
        guess = input("Gissa en bokstav: ").upper()
        guessed_letter.append(guess)
        if guess in correct_word_list:
            result = "Rätt bokstav"
            
            # ul_word_list.clear()
            for i in range(len(correct_word_list)):
                if correct_word_list[i] == guess:
                    ul_word_list[i] = guess


        else:
            result = "Fel bokstav"
            game.level += 1

        