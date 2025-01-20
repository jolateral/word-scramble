import random

"""This the main file of the word scramble game.
This program specficially reviews while loops, for loops, and the list data type."""

# initiate a random list of words
word_list = ["apple", "quantum", "umbrella", "spider", "orange"]

"""This function is the start to the game."""
def run_game() -> None:
    # choose the answer
    answer = random.choice(word_list)

    # initiate the player's answer list
    guess_so_far = []
    for i in range(len(answer)):
        guess_so_far.append("_")

    # start the game!
    print("Let's play Hangman! To guess a word, type 'word'. If you want to guess a letter, type 'letter.")

    action = input()

    if action == "letter":  # the player guesses a letter
        print("What letter would you like to guess?")
        guess = input()

        if guess in answer:
            counter = 0
            for i in answer:
                if i == guess:
                    guess_so_far[counter] = guess
                counter += 1
            
            print("Good job! Here's your progress so far:")
            print(guess_so_far)

    elif action == "word":
        print("What word would you like to guess?")
        guess = input()

        # compare the guess with the answer
        if guess == answer:
            print("You got it! The answer was " + answer)
            return
        else:   # the guess is not correct
            ...
