# Mike Wilson 14 Feb 2022
# This program iterates the given list of number and prints the ones divisible by five

num_list = [10, 20, 33, 46, 55]

print("Given list:", num_list)
print('Divisible by 5:')
for num in num_list:
  if num % 5 == 0:
    print(num)

    