# Program #1: Random Dice
# Author: Abrielle Nyei
# Date: 02/27/2026
# Description:
# This program simulates rolling two dice 100 times.
# The randDice() function generates two random numbers between 1 and 6,
# returns their sum, and the mainline calculates the average of 100 rolls.

import random

def randDice():
    # Generate 2 random numbers between 1 and 6 (inclusive)
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Sum the 2 numbers
    dice_sum = die1 + die2

    # Return sum to calling function
    return dice_sum


#########
# Mainline
total = 0

# Call randDice() 100 times
for i in range(100):
    total += randDice()

# Calculate average
average = total / 100

# Print average rounded to nearest 0.01
print("Average of 100 dice rolls:", round(average, 2))
