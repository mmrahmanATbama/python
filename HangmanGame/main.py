import random
# import only system from os
from os import system, name



# define our clear function
def clear():
  # for windows
  if name == 'nt':
    _ = system('cls')

from  hangman_words import word_list
from hangman_art import stages, logo
chosen_word = random.choice(word_list)
print(logo)
print(chosen_word)
chosen_word_length = len(chosen_word)
num = 0
display = []
lives = 6


while num < chosen_word_length:
  display.append("-")
  num += 1

while ("-" in display) and (lives > 0):
  guess = input("Guess a letter: ").lower()
  clear()

  if (guess in display):
    print(f"You have already guessed {guess}. choose again.")

  count = 0
  for letter in chosen_word:
    if (guess == letter):
      display[count] = guess

    count += 1

# above can be done this way:
#for position in range(chosen_word_length):
  #   letter = chosen_word[position]
  # if letter == guess:
    #display[position] = letter
#print(display)
  if("-" not in display):
    print("You win.")
  if (guess not in chosen_word):
    lives -= 1
    print(f"Letter '{guess}' is not in the word. You lost a life.")
    if(lives == 0):
        print("You lose")

      #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  print(stages[lives])


