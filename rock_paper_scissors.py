# Mike Wilson 5 July 2021
# This program emulates a game of Rock Paper Scissors and allows for user input.

def get_user_choice():
  """Gets the user's choice"""
  user_input = input("Please type 'rock', 'paper', or 'scissors'.: ")
  user_choice = user_input.lower()
  if (user_choice == 'rock') or (user_choice == 'paper') or (user_choice == 'scissors'):
    print(f"You have selected {user_choice}.")
  else:
    print("Please restart the program and pick either rock, paper, or scissors.")
