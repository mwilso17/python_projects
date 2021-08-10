# Mike Wilson 9 August 2021
# This program executes the main portion of the code for the Kiosk program

from inventory import inventory, basket, subtotal

# Tax rate can be changed by changing the value. Ie: 0.08 = 8% tax rate
tax_rate = 0.08

def calculate_total():
  """Accepts user input, calculates subtotal, adds tax, rounds total."""
  active = True
  while active:
    user_input = input('Enter your next item (q to stop, i for inventory): ')

    if user_input == 'q':
      active = False
    elif user_input == 'i':
      print(inventory)
      user_input
    elif user_input not in inventory:
      print('Please try again with an item we have in stock')
      user_input
    elif user_input in inventory:
      print(f'Adding your {user_input} to the cart.')
      basket.append(user_input)

  print('Your cart contains: ', basket)

  for items in basket:
    subtotal.append(inventory[items])
  pre_tax_total = sum(subtotal)

  amount_to_pay = round(pre_tax_total + (pre_tax_total*tax_rate), 2)

  print(f"Your total is: $", amount_to_pay)

# Executes code
calculate_total()