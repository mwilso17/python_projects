# Mike Wilson 13 September 2021
# This program simulates how a player character may ask a non-player-character
# (NPC) multiple questions and get a different result each time.

# Empty inventory list to add an item to if enough questions are asked.
player_inventory = []

# function to call when the player interacts with/questions an NPC.
def question_npc():
  while True:
    questions_asked = 0
    if questions_asked == 0:
      print("Welcome traveler! Stay in our small village as long as you want.")
      questions_asked = questions_asked + 1
      print(questions_asked)
      break

    elif questions_asked == 1:
      print("You should probably talk to the village elder.")
      questions_asked = questions_asked + 1
      print(questions_asked)
      break


    if questions_asked == 2:
      print("You can have this. The baker gave me an extra one today.")
      player_inventory.append('sweet roll')
      questions_asked = questions_asked + 1
      print(questions_asked)
      break


    if questions_asked == 3:
      print("Take care, traveler.")
      print(questions_asked)
      break

print(player_inventory)
question_npc()
question_npc()
print(player_inventory)
