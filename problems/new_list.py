# Mike Wilson 14 Feb 2022
# Create a new list from 2 lists using a condition

from unittest import result


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def merge_list(list1, list2):
  result_list = []

  # iterate the first list
  for num in list1:
    # check if current number is odd
    if num % 2 != 0:
      # add odd number to result list
      result_list.append(num)

  # iterate the second list
  for num in list2:
    # check if current number is even
    if num % 2 == 0:
      # add even number to result list
      result_list.append(num)
  
  return result_list


print("result liust: ", merge_list(list1, list2))