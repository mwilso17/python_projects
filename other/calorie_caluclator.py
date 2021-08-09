# Mike Wilson 5 July 2021
# A mini app to figure out how calories consumed in a week measure against
# ideal calorie consumption.

def input_calories_by_day(day):
  if day == 'Monday':
    return 3000
  if day == 'Tuesday':
    return 1700
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

def get_total_calories():
  return input_calories_by_day('Monday') + input_calories_by_day('Tuesday') + input_calories_by_day('Wednesday') + input_calories_by_day('Thursday') + input_calories_by_day('Friday') + input_calories_by_day('Saturday') + input_calories_by_day('Sunday')

def get_ideal_calories():
  ideal_daily_calories = 2000
  return ideal_daily_calories * 7

def calculate_health_plan():
  actual_calories = get_total_calories()
  ideal_calories = get_ideal_calories()
  if actual_calories == ideal_calories:
    print("You ate just the right amount this week.")
  if actual_calories > ideal_calories:
    print("You ate too much this week. Go work out!")
  if ideal_calories > actual_calories:
    print("You ate less than ideal. Go eat some more.")

calculate_health_plan()