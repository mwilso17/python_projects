# Mike Wilson 7 Feb 2022
# This program takes a string and removes a set number of characters from it.

def remove_characters(string, number):
  print('Original String: ', string)
  x = string[number:]
  return x

print('Removing characters from a string')
print(remove_characters('pynative', 4))