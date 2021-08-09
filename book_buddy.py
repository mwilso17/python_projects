# Mike Wilson 9 August 2021
# This is a mini-application that analyzes a .txt file for its length in words.
# It also takes user input to determine how long it will take to read the .txt
# file.

#Here is where you can add in any .txt file on your computer. As long as the 
# path to the .txt file is set here correctly, the rest of the program
# won't need to be altered. If viewing this program from my GitHub,
# you can use the sample text, 'wonderland.txt' in txt_files.
filename = 'txt_files\wonderland.txt'

def calculate_read_time(filename):
  '''Calculates the reading time for a file.'''
  # Get user input for reading speed and time reading per day. Convert it
  # to an integer
  reading_speed = input('Enter your reading speed in wpm (200 is average): ')
  reading_speed = int(reading_speed)
  time_per_day = input('How many minutes a day do you plan on reading?: ')
  time_per_day = int(time_per_day)

  # code that opens and analyzes the file.
  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  except FileNotFoundError:
    print('File was not found. Please enter a different file')
  else:
    words = contents.split()
    num_words = len(words)
    print(f"There are roughly {num_words} words in {filename}.")

  # Mathmatical calculation of inputs. Rounds to nearest whole number
  days_till_completion = round(num_words/(reading_speed*time_per_day))
  print(f'It will take you about {days_till_completion} days to finish this text.')



if __name__ == '__main__':
  calculate_read_time(filename)
