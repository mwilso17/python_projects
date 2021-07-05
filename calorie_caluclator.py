# Mike Wilson 5 July 2021
# A mini app to figure out how calories consumed in a week measure against
# ideal calorie consumption.

def input_calories_by_day(day):
  if day == 'Monday':
    return 3500
  if day == 'Tuesday':
    return 1800
  if day == 'Wednesday':
    return 1500
  if day == 'Thursday':
    return 1800
  if day == 'Friday':
    return 2200
  if day == 'Saturday':
    return 2000
  if day == 'Sunday':
    return 1700
  else:
    return 'please submit a valid day'

