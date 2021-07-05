# Mike Wilson 5 July 2021
# This program emulates a game of Rock Paper Scissors and allows for user input.

def get_user_choice():
  """Gets the user's choice"""
  user_input = input("Please type 'rock', 'paper', or 'scissors'.: ")
  user_choice = user_input.lower()
  if user_choice == 'rock' or 'paper' or 'scissors':
    print(f"You have selected {user_choice}.")
  else:
    print("Please select either rock, paper, or scissors.")

