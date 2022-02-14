# Mike Wilson 14 Feb 2022
# This program extracts each digit from an integer in reverse order

number = 7536
print("Given number", number)
while number > 0:
  # get the last digit
  digit = number % 10
  # remove last digit and repeat loop
  number = number // 10
  print(digit, end=" ")


