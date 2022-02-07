# Mike Wilson 7 Feb 2022
# This program accepts a string and prints the items listed at an even index number

userString = 'ThisIsALongStringWithoutSpaces'

size = len(userString)

def string_splitter(str):
  for i in range(0, size - 1, 2):
    print("index[", i,"]", str[i])


string_splitter(userString)