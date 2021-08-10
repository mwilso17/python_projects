# Mike Wilson 9 August 2021
# This file contains the inventory list for the kiosk mini app
# inventory is stored in format: 'item name': price


inventory = {
  'apple': 0.59,
  'soda': 1.19,
  'magazine': 6.39,
  'beer': 2.19,
}

subtotal = []
basket = []

def calculate_subtotal():
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
  amount_to_pay = sum(subtotal)

  print(f"Your total is: $", amount_to_pay)

calculate_subtotal()