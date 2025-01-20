import random

"""This the main file of the word scramble game.
This program specficially reviews while loops, for loops, and the list data type."""

# initiate a random list of words
word_list = ["apple", "quantum", "umbrella", "spider", "orange"]

"""This function is the start to the game."""
def run_game() -> None:
    # set up the lives and if the player has won
    lives = 5
    status = "lose"

    # initiate the answer
    answer = random.choice(word_list)
    answer_list = []
    for i in range(len(answer)):
        answer_list.append(answer[i])

    # initiate the player's progress
    progress = []
    for i in range(len(answer)):
        progress.append('_')

    # introduce the game
    print("Hello, let's play Hangman!")

    while lives != 0 and (progress != answer_list):
        print('Current progress:', progress)
        print("Lives remaining:", lives)
        # let the player choose what action to do
        print('Would you like to guess a letter or a word?')
        action = input()
        
        if action == 'letter':
            # the player wants to guess a letter
            print("What leter would you like to guess?")
            guess = input()

            if guess in answer:
                # the letter is in the answer!
                # update progress
                for i in range(len(answer)):
                    if guess == answer_list[i]:
                        progress[i] = guess

                print("Good job! The letter is in the word")
                continue

            else:
                # the letter is not in the answer
                print("Sorry! That's not in the answer")
                lives -= 1

        elif action == 'word':
            print("What word would you like to guess?")
            guess = input()

            if answer == guess:
                print("Good job! You won the game!")
                progress = answer_list
                break
            
            else:
                print("Sorry, that's not the answer!")
                lives -= 1

        else:
            print("Thats not a valid answer! You must type either 'letter' or 'word")
            continue

    if progress == answer_list:
        print("Congrats, you won the game!!")
    if progress != answer_list:
        print("Sorry, you lost :(")
            
            

        