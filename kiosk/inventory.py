# Mike Wilson 9 August 2021
# This file contains the inventory list for the kiosk mini app
# inventory is stored in format: 'item name': price


inventory = {
  'apple': 0.59,
  'soda': 1.19,
  'magazine': 6.39,
  'beer': 2.19,
}

def calculate_subtotal():
  subtotal = []
  active = True
  for item, price in inventory.items():
    while active:
      cart = input('Enter your next item (q to stop, i for inventory): ')

      if cart == 'q':
        active = False
      elif cart == 'i':
        print(inventory)
        cart
      elif cart != item:
        print('Please try again with an item we have in stock')
        cart
      elif cart == item:
        print(f'Adding your {item} to the cart.')
        subtotal.append(price)

  Sum = sum(subtotal)
  print(Sum)

calculate_subtotal()