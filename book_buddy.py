# Mike Wilson 9 August 2021
# This is a mini-application that analyzes a .txt file for its length in words.
# It also takes user input to determine how long it will take to read the .txt
# file.

filename = 'txt_files\wonderland.txt'

def calculate_read_time(filename):
  reading_speed = input('Enter your reading speed in wpm (200 is average): ')
  reading_speed = int(reading_speed)
  time_per_day = input('How many minutes a day do you plan on reading?: ')
  time_per_day = int(time_per_day)

  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  except FileNotFoundError:
    print('File was not found. Please enter a different file')
  else:
    words = contents.split()
    num_words = len(words)
    print(f"There are roughly {num_words} words in {filename}.")

  days_till_completion = round(num_words/(reading_speed*time_per_day))
  print(f'It will take you about {days_till_completion} days to finish this text.')



if __name__ == '__main__':
  calculate_read_time(filename)
