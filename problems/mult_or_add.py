# Mike Wilson 7 Feb 2022
# This program takes two numbers and multiplies them together, only if their product
# is above 100. Otherwise, it returns the sum of the two numbers.

def mult_or_add(num1, num2):
  product = num1 * num2
  sum = num1 + num2
  if product >= 100:
    print('The product of your two numbers is greater than 100.')
    print(f'{num1} times {num2} is: {product}')
  else:
    print('The product of your numbers is less than 100, so we added them instead')
    print(f'{num1} plus {num2} is: {sum}')


mult_or_add(10, 50)
mult_or_add(1, 4)