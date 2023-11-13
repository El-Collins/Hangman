import random
import os

# print(logo)

from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)
# print(chosen_word)

word_length = len(chosen_word)
end_of_game = False
lives = 6
display = []

for _ in range(word_length):
  display += "_"
print(display)

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  # os.system('clear')
  # print(logo)

  if guess in display:
    print("You have already entered this letter")

  if guess not in chosen_word:
    print("Wrong letter, you've lost a live")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose!")

  for position in range(word_length):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter

  print(f"{' '.join(display)}")
  # print(display)

  if "_" not in display:
    end_of_game = True
    print("You win!")

  print(stages[lives])
