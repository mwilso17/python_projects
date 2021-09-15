# Mike Wilson 15 September 2021
# This program uses random in order to read tarot cards to a user.
# Definitions of each card will be stored in a seperate README.txt file.
import random

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