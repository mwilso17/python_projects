# Mike Wilson 5 July 2021
# This program emulates a game of Rock Paper Scissors and allows for user input.

import math
import random

def get_user_choice():
  """Gets the user's choice"""
  user_input = input("Please type 'rock', 'paper', or 'scissors'.: ")
  user_choice = user_input.lower()
  if (user_choice == 'rock') or (user_choice == 'paper') or (user_choice == 'scissors'):
    print(f"You have selected {user_choice}.")
    return user_choice
  else:
    print("Please restart the program and pick either rock, paper, or scissors.")

def get_computer_choice():
  """Gets the computers choice of rock, paper, or scissors."""
  randomNumber = math.floor(random.uniform(0, 3))
  if randomNumber == 0:
    return 'rock'
  elif randomNumber == 1:
    return 'paper'
  elif randomNumber == 2:
    return 'scissors'

def determine_winner(user_choice, computer_choice):
  """Determines the winner of the match."""
  # In case of a tie
  if user_choice == computer_choice:
    return "It is a tie"

  # If user chooses rock
  if user_choice == 'rock':
    if computer_choice == 'scissors':
      return 'Rock beats scissors. User wins!'
    else:
      return 'Paper beats rock. Computer wins!'

  # If user chooses paper
  if user_choice == 'paper':
    if computer_choice == 'rock':
      return "Paper beats rock. User wins!"
    else:
      return "Scissors beats paper. Computer wins!"

  # If user chooses scissors
  if user_choice == 'scissors':
    if computer_choice == 'paper':
      return "Scissors beats paper. User wins!"
    else:
      return "Rock beats scissors. Computer wins!"

 
print(determine_winner('rock', 'rock'))
print(determine_winner('scissors', 'paper'))
print(determine_winner('rock', 'paper'))