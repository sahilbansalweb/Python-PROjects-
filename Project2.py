"""
|---------------------------------------------<  MINI PROJECT => 2  >--------------------------------------------------\
|--------------------------------------------<  STONE PAPER SCISSOR  >-------------------------------------------------\
"""
import random

print("Here,We have to follow some Rules to play this awesome game :::> ")
print("These are the some keys to be entered by user :------")
print("                 For Rock :- R")
print("                For Paper :- P")
print("               For Scissor :- S")

print(" ")
n = input("Enter Your choice:- ")
n.upper()
if n == 'R' or n == 'P' or n == 'S':
    ch = ['R', 'P', 'S']
    comp = random.choice(ch)
    if comp == n:
        print("Congratulations u won from me (*_*) ")
        print("I am loser and you are winner")
    else:
        print("Sorry, But you LOST ")
        print("you can  easily win have a enjoyment here")
    print("THANKS FOR PLAYING, KEEP SUPPORTING YOUR CREATER")
else:
    print("Sorry,But u entered a wrong choice please try again")



