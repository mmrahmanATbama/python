import random

# Declare constant for guess type.
EASY = 10
HARD = 5
# get a random number from 1 to 100
NUMBER_CHOSEN = random.randint(1, 100)


# Welcome message:
def start_game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct number is: {NUMBER_CHOSEN}")
    difficulty_level = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()

    if difficulty_level != 'easy' and difficulty_level != 'hard':
        print("invalid option")
        return
    if difficulty_level == 'easy':
        return EASY
    elif difficulty_level == 'hard':
        return HARD


# still chances left?ask the user for input, else you lose.
def user_input():
    chance_left = start_game()
    print(chance_left)
    are_chances_left = True

    while are_chances_left:
        print(f"You have {chance_left} attempt to guess the number.")
        guessed_number = int(input("Make a guess: "))
        if guessed_number > NUMBER_CHOSEN:
            print("Too high")
            print("Guess again")
        elif guessed_number < NUMBER_CHOSEN:
            print("Too low")
            print("Guess again")
        elif guessed_number == NUMBER_CHOSEN:
            print(f"You got it! The answer was {NUMBER_CHOSEN}")
            are_chances_left = False
        chance_left -= 1
        if chance_left == 0:
            are_chances_left = False
            print("You've run out of guesses, you lose")


user_input()
