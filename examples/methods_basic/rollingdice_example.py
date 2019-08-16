
# Craps.

import random

def rollDice():
   die1 = random.randrange( 1, 7 )
   die2 = random.randrange( 1, 7 )
   workSum = die1 + die2
   print("Player rolled %d + %d = %d" % ( die1, die2, workSum ))

   return workSum

sum = rollDice()                          # first dice roll

if sum == 7 or sum == 11:                 # win on first roll
   gameStatus = "WON"
elif sum == 2 or sum == 3 or sum == 12:   # lose on first roll
   gameStatus = "LOST"
else:                                     # remember point
   gameStatus = "CONTINUE"
   myPoint = sum
   print("Point is", myPoint)
   
while gameStatus == "CONTINUE":   # keep rolling
   sum = rollDice()

   if sum == myPoint:             # win by making point
      gameStatus = "WON"
   elif sum == 7:                  # lose by rolling 7:
      gameStatus = "LOST"

if gameStatus == "WON":
   print("Player wins")
else:
   print("Player loses")
  
