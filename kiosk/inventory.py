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
  for item, value in inventory.items():
    while active:
      message = input('Enter your next item (q to stop adding items): ')

      if message == 'q':
        active = False
      else:
        print(f'Adding your {item} to the cart.')
        subtotal.append(value)

  print(subtotal)

calculate_subtotal()