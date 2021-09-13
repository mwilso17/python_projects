# Mike Wilson 13 September 2021
# This program simulates how a player character may ask a non-player-character
# (NPC) multiple questions and get a different result each time.

# Empty inventory list to add an item to if enough questions are asked.
player_inventory = []

# function to call when the player interacts with/questions an NPC.
def question_npc(questions_asked):
  while True:
    if questions_asked == 0:
      print("Welcome traveler! Stay in our small village as long as you want.")
      break

    if questions_asked == 1:
      print("You should probably talk to the village elder.")
      break


    if questions_asked == 2:
      print("You can have this. The baker gave me an extra one today.")
      player_inventory.append('sweet roll')
      break

    if questions_asked == 3:
      print("Take care, traveler.")
      break

# bring up initial inventory
print(player_inventory)
question_npc(0)
question_npc(1)
question_npc(2)
question_npc(3)

# Bring up inventory again to make sure item was added
print(player_inventory)
