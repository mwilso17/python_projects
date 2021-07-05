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
