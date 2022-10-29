from random import choice
from hangman_wordlist import word_list
from art import logo, stages

# Initial setup
lives = 6
print(logo)
chosen_word = choice(word_list)
display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"

# Game loop
while True:
    guess = input("Enter a letter: ").lower()

    if guess in display:
        print("You've already guessed '{}'".format(guess))

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            print("You lost!")
            break
        print("Your guess was '{}', that's not in the word. You lose a life.".format(guess))

    print(display)

    if "_" not in display:
        print("You won!")
        break

    print(stages[lives])
