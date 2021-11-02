# Mike Wilson 15 September 2021
# This program uses random in order to read tarot cards to a user.
# Definitions of each card will be stored in a seperate README.txt file.
import random, time

# Lists to stor major and minor arcana.
major_arcana = ['The Fool',
  'The Magician',
  'The High Priestess',
  'The Empress',
  'The Emperor',
  'The Hierophant',
  'The Lovers',
  'The Chariot',
  'Justice',
  'The Hermit',
  'The Wheel of Fortune',
  'Strength',
  'The Hanged Man',
  'Death',
  'Temperance',
  'The Devil',
  'The Tower',
  'The Star',
  'The Moon',
  'The Sun',
  'Judgement',
  'The World']

minor_arcana = ['The 1 of Cups', 'The 2 of Cups', 'The 3 of Cups',
  'The 4 of Cups', 'The 5 of Cups', 'The 6 of Cups', 'The 7 of Cups',
  'The 8 of Cups', 'The 9 of Cups', ' The 10 of Cups', 'The Page of Cups',
  'The Queen of Cups', 'The King of Cups', 'The Knight of Cups', 
  'The 1 of Pentacles', 'The 2 of Pentacles', 'The 3 of Pentacles',
  'The 4 of Pentacles', 'The 5 of Pentacles', 'The 6 of Pentacles',
  'The 7 of Pentacles', 'The 8 of Pentacles', 'The 9 of Pentacles',
  'The 10 of Pentacles', ' The Page of Pentacles', 'The Queen of Pentacles',
  'The King of Pentacles', 'The Knight of Pentacles', 'The 1 of Wands',
  'The 2 of Wands', 'The 3 of Wands', 'The 4 of Wands', 'The 5 of Wands',
  'The 6 of Wands', 'The 7 of Wands', 'The 8 of Wands', 'The 9 of Wands',
  'The 10 of Wands', 'The Page of Wands', 'The Queen of Wands', 'The King of Wands',
  'The Knight of Wands', 'The 1 of Swords', 'The 2 of Swords', 'The 3 of Swords',
  'The 4 of Swords', 'The 5 of Swords', 'The 6 of Swords', 'The 7 of Swords',
  'The 8 of Swords', 'The 9 of Swords', 'The 10 of Swords', 'The Page of Swords',
  'The Queen of Swords', 'The King of Swords', 'The Knight of Swords']


# Function to get Shiva's Trident (3 Major arcana for past present and future,
# 2 Minor arcana for strengths and weaknesses)
def shivas_trident():
  past = major_arcana[random.randint(0, len(major_arcana) - 1)]
  major_arcana.remove(past)
  present = major_arcana[random.randint(0, len(major_arcana) - 1)]
  major_arcana.remove(present)
  future = major_arcana[random.randint(0, len(major_arcana) - 1)]
  major_arcana.remove(future)
  strength = minor_arcana[random.randint(0, len(minor_arcana) - 1)]
  minor_arcana.remove(strength)
  weakness = minor_arcana[random.randint(0, len(minor_arcana) - 1)]
  minor_arcana.remove(weakness)

  print('Think deeply of your question. Your cards will be read in 5 seconds.')
  time.sleep(6)

  print('Your Past: ' + past)
  time.sleep(3)
  print('Your Present: ' + present)
  time.sleep(3)
  print('Your Future: ' + future)
  time.sleep(3)
  print('Your Strength: ' + strength)
  time.sleep(3)
  print('Your Weakness: ' + weakness)
  time.sleep(3)
  
  print('Reflect on this reading and yourself. Go in peace. So mote it be.')


def three_card_spread():
  deck = (major_arcana + minor_arcana)
  past = deck[random.randint(0, len(deck) - 1)]
  present = deck[random.randint(0, len(deck) - 1)]
  future = deck[random.randint(0, len(deck) - 1)]

  print(past)
  print(present)
  print(future)



# Comment out all but whichever spread you want to use.
# shivas_trident()
three_card_spread()

# Test to make sure GitHub is still connected