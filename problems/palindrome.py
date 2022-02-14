# Mike Wilson 14 Feb 2022
# This program checks to see if a number is a palindrome number or not


def palindrome(number):
  print("original number", number)
  original_num = number

  # Reverse the given number
  reverse_num = 0
  while number > 0:
    reminder = number % 10
    reverse_num = (reverse_num * 10) + reminder
    number = number // 10

  if original_num == reverse_num:
    print("Given number is a palindrome")
  else:
    print("Given number is not a palindrome")

palindrome(121)
palindrome(124)