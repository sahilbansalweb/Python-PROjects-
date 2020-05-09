"""
                       -----------------------------: MINI PROJECT :------------------------------------
                                                        CASINO
"""
import random
print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ W E L C O M  E    TO    C A S I N O ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")

tcash = int(input("\n\n\n\n\n\n How Much Amount do you have in your pocket for casino ??????  "))
ch = 'y'
while (ch == 'y' or ch == 'Y') and tcash > 1:
    icash = int(input("\n\nSo, Brother How much cash do you like to play in this turn ?   "))
    while icash > tcash :
        print("Please Enter Valid amount ")
        icash = int(input("\n So, How much cash do you like to play in this turn ?   "))
    tcash = tcash - icash
    number = random.randrange(0, 10)
    user_input = int(input("Now, Tell ur Lucky Number for Casino Play (Between 0 to 10)  ?  "))
    while user_input < 0 or user_input > 10:
        print("Sorry Brother, You Entered a wrong choice Please TRY again")
        user_input = int(input("Now, Tell ur Lucky Number for Casino Play (Between 0 to 10)  ?  "))
    else:
        print("The Number was :-",number )
        if user_input == number:
            print("\n\n You Won this match u are extremely lucky !!!!")
            tcash = tcash + icash*3
        else:
            print("\n\n Sorry! Bad Luck in this match")
    print("Current Total Cash is :", tcash)
    ch = input("Do u like to play again and try your luck ?????(y/n) ")


if tcash < 1:
    print("\n\nSorry Out of Money")

print("At the End, Total money that u have is: ", tcash)
