# Mike Wilson 16 November 2021
# This program creates an interactive dictionary using python
# you will need the data.json file located in this folder to run this
# application properly.
import json
data = json.load(open("applications\data.json"))

def translate(word):
  word = word.lower()
  if word in data:
    return data[word]
  else:
    return "That word doesn't exist. Please check it."

word = input("Enter word: ")

print(translate(word))