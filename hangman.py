import random

# ASCII ART CREDIT: https://ascii.co.uk/art/hangman

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

file = open("words.txt", "r")

words = []
for line in file:
    words.append(line[0:len(line) - 1])

word = random.choice(words)

none = '''
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
 jgs_|___
'''

one = '''
      _______
     |/      |
     |      (_)
     |     
     |       
     |      
     |
 jgs_|___
'''

two = '''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
 jgs_|___
'''

three = '''
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
 jgs_|___
'''

four = '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 jgs_|___
'''

five = '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      | 
     |
 jgs_|___
'''

six = '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      | |
     |
 jgs_|___
 '''

wrong_count = 0
hangmans = [none, one, two, three, four, five, six]
# storing all the correctly guessed letters
letters = []
# to store incorrect letters, preventing user from guessing same letter twice
incorrect_letters = []
# if the user has already guessed the word
correct = False

while wrong_count < 6 and not correct:
    printed = ""
    for i in range(len(word)):
        if word[i] in letters:
            printed += word[i]
        else:
            printed += "_"
    print(hangmans[wrong_count])
    print(printed)
    valid = False
    guess = ""
    while not valid:
        guess = input("Please enter your guess: ")
        guess = guess.lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Try again.")
        elif guess in incorrect_letters:
            print("You've already guessed this letter! Try again.")
        else:
            valid = True
    if guess in word:
        letters.append(guess)
        # prevent user from guessing same letter twice
        incorrect_letters.append(guess)
        print("Your guess was correct!\n")
        for i in range(len(word)):
            if not word[i] in letters:
                break
            elif i == (len(word) - 1):
                correct = True
    else:
        wrong_count += 1
        print("Your guess was incorrect!\n")
        incorrect_letters.append(guess)

if wrong_count == 6:
    print(hangmans[6])
    print(f'You lost! The word was "{word}." Better luck next time!')
else:
    print(f'Congratulations! You\'ve guessed the word "{word}"!')
