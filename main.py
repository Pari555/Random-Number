import random

print("Coin Flip")

# 1 = heads, 2 = tails
coin = random.randint(1,2)

if(coin == 1):
  print("It's Heads!")
else:
  print("It's Tails!")

print("Dice Roll")

# Exercise: Create a code that mimics a dice roll using random numbers. The code should print out what number is "rolled", letting the user know what the result is.

diceRoll = random.randint(1,6)

if(diceRoll == 1):
  print("You landed on 1")
elif(diceRoll == 2):
  print("You landed on 2")
elif(diceRoll == 3):
  print("You landed on 3")
elif(diceRoll == 4):
  print("You landed on 4")
elif(diceRoll == 5):
  print("You landed on 5")
elif(diceRoll == 6):
  print("You landed on 6")

