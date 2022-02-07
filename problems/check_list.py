# Mike Wilson 7 Feb 2022
# This program checks to see if the first and last entries of a list are equivalent

list_1 = [10, 20, 30, 40, 50, 10]
list_2 = [1, 2, 3, 3, 4, 7, 5, 32, 4]

def first_and_last(list):
  if list[0] == list[-1]:
    print(f'{list} has equivalent values for it\'s first and last entries')
  else:
    print(f'{list} does not have equivalent values for it\'s first and last entries')


first_and_last(list_1)
first_and_last(list_2)