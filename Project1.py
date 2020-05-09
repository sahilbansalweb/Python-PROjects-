"""
Bhai ye h mera project 1 in python sirf try k liye h agar kuch improvements vegara karne honge to bta dena github k help se , so have a good day with me.
                       -----------------------------: MINI PROJECT :------------------------------------
                                                    GUESS THE NUMBER
"""

import random
import sys

number=random.randrange(0, 20)
user_input = int(input())
if user_input < 0 or user_input > 20:
    print("Sorry Brother, YOU Entered a wrong choice Please TRY again")
    print("Wish You a good day! and have fun with me")
    exit()
else:
    if user_input == number:
        print("Bro, You Won this match u are extremely lucky !!!!")
        print("WINNER WINNER GAME WINNER")
    else:
        if user_input < number:
            print("Your Guess is too low !!! ")
        else:
            print("Your number is higher than me !!! ")
