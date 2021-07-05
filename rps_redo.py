# Mike Wilson 5 July 2021
# Rock Paper Scissors emulator. 

def get_user_choice(user_input):
  user_input = user_input.lower()
  if (user_input == 'rock') or (user_input == 'paper') or (user_input == 'scissors'):
    return user_input
  else:
    return 'Please enter a valid option'

