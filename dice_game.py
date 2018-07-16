from random import randint
from time import sleep


"""
This program will allow user to roll a pair of dice. 
Add values  of the roll. 
Ask the user to guess a number.
Compare the user's guess to the total value. 
Determine the winner (user or computer)
"""

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess
  
  
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2 
  print "The maximum possible value is %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "Guess exceeds max_val. Please play again."
  else:
      print "Rolling..."
      sleep(2)
      print "The first roll is: %d" % first_roll
      sleep(1)
      print "The second roll is: %d" % second_roll
      sleep(1)
      total_roll = first_roll + second_roll
      print "The total value is: %d" % total_roll
      print "Result..."
      sleep(1)
      
      if guess == total_roll:
        print "You won!"
        return "WON"
      else: 
        print "You lost"
        return "LOST"
      
roll_dice(6)
 