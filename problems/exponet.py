# Mike Wilson 14 Feb 2022
# This program returns an int value of base raised to the power of the exp.

def exponent(base, exp):
  num = exp
  result = 1
  while num > 0:
    result = result * base
    num = num - 1
  print(base, "raises to the poer of", exp, "is: ", result)


exponent(5, 4)