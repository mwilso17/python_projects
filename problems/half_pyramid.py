# Mike Wilson 14 Feb 2022
# Prints a half-pyramid pattern with the asterisk

for i in range(6, 0 , -1):
  for j in range(0, i - 1):
    print("*", end=' ')
  print(" ")

