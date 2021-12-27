import csv
from datetime import date, datetime

import matplotlib.pyplot as plt

filename = 'data\sitka_weather_2018_simple.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)

  # Get high temps from file and dates
  dates, highs, lows = [], [], []
  for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[5])
    low = int(row[6])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

  # Plot the high and low temps.
  plt.style.use('seaborn')
  fig, ax = plt.subplots()
  ax.plot(dates, highs, c='red')
  ax.plot(dates, lows, c='blue')

  # Format plot.
  ax.set_title('Daily high and low temps - 2018', fontsize=24)
  ax.set_xlabel('', fontsize=16)
  fig.autofmt_xdate()
  ax.set_ylabel('Temperature (F)', fontsize=16)
  ax.tick_params(axis='both', which='major', labelsize=16)

  plt.show()