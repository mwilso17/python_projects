# Mike Wilson 15 September 2021
# This program uses pyinputplus, random, and time to create a short quiz
# that asks users to add three numbers together quickly
import pyinputplus as pyip
import random, time

# Number of questions in the quiz
questions = 10

# Stores correct answers
correctAnswers = 0

# Main loop for the program
for questionNumber in range(questions):
  num1 = random.randint(0, 20)
  num2 = random.randint(0, 20)
  num3 = random.randint(0, 20)

  prompt = '#%s: %s + %s + %s = ' % (questionNumber, num1, num2, num3)

  try:
    pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 + num2 + num3)],
    blockRegexes=[('.*', 'Incorrect!')],
    timeout=10, limit=3) #timeout=10 seconds to answer, limit= 3 tries
  except pyip.TimeoutException:
    print('You took too long!')
  except pyip.RetryLimitException:
    print('You took too many tries!')
  else:
    print('Great job!')
    correctAnswers += 1
  time.sleep(1) # Gives users 1 second to view answer before next question pops up
print('Score: %s / %s' % (correctAnswers / questions))