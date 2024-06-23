import random
from re import U
# words = ["UMBRELLA", "COMPUTER","TELESCOPE","SMARTPHONE"]
f = open("words.txt", "r") # to open a file in read mode, r represents read mode
data = f.readline() # to get words/data from file, it comes in list form
words = data.split() # words/data is seprated from spaces

word = random.choice(words)
word = word.upper() # to convert the words from lower to upper case from file


total_chances = 7
guessed_word = "-" * len(word)

while total_chances !=0:
    print(guessed_word)
    letter = input("Guess a letter:").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
                print(guessed_word)
        
        if guessed_word == word:
            print("congratulations you won!!!")
            break
    else:
        total_chances -= 1
        print("Incorrect guess")
        print("The remaining chances are: ", total_chances)

else:
    print("Game Over")
    print("You Lose")
    print("All the chances are exhausted")

print("The correct word is:", word)