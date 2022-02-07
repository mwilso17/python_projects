# Mike Wilson 7 Feb 2022
# This program loops through a set of numbers and adds the current number to the previous
# number and prints them.

def sum_sequence(number):
  for i in range(number):
    if i == 0:
      print(f'Current: {i}. Previous: {i}. Sum: {i}')
    else:
      print(f'Current: {i}. Previous: {i - 1}. Sum: {i + (i-1)}')



sum_sequence(10)