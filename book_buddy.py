# Mike Wilson 9 August 2021
# This is a mini-application that analyzes a .txt file for its length in words.
# It also takes user input to determine how long it will take to read the .txt
# file.

filename = 'txt_files\wonderland.txt'

try:
  with open(filename, encoding='utf-8') as f:
    contents = f.read()
except FileNotFoundError:
  print('File was not found. Please enter a different file')
else:
  words = contents.split()
  num_words = len(words)
  print(f"The file {filename} has about {num_words} words.")