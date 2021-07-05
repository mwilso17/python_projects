# Mike Wilson 5 July 2021
# Rock Paper Scissors emulator. 

import math
import random

def get_user_choice(user_input):
  user_input = user_input.lower()
  if (user_input == 'rock') or (user_input == 'paper') or (user_input == 'scissors'):
    return user_input
  else:
    return 'Please enter a valid option'

def get_computer_choice():
  random_number = math.floor(random.uniform(0, 3))
  if random_number == 0:
    return 'rock'
  if random_number == 1:
    return 'paper'
  if random_number == 2:
    return 'scissors'

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return 'It is a tie'
  if user_choice == 'rock':
    if computer_choice == 'paper':
      return 'Paper covers rock. Computer wins.'
    else:
      return 'Rock beats scissors. User wins.'
  if user_choice == 'paper':
    if computer_choice == 'scissors':
      return 'Scissors cut paper. Computer wins.'
    else:
      return 'Paper covers rock. User wins.'
  if user_choice == 'scissors':
    if computer_choice == 'rock':
      return 'Rock crushes scissors. Computer wins.'
    else:
      return 'Scissors cuts paper. User wins.'
