#########################################################
# Name: Parsa Jahanlou
# Date: Due July 1st, 2020
# Description: A Foolproof Game
#########################################################

# Import randint to randomize the coin and other things
from random import randint

# Asking the user for how many games they want to run
games = int(input("How many games?"))
# Asking the user how many coin tosses they want
coins = int(input("How many coin tosses per game?"))

# Setting up some basic global variables
x = 0
totalAWins = 0
totalBWins = 0
totalCWins = 0
totalAPer = 0
totalBPer = 0
totalCPer = 0

# Coin toss function that tosses the coin and does all the countings
def coinToss(coins):

    # Local variables for counting the heads and tails for each game
    groupAWins = 0
    groupBWins = 0
    groupCWins = 0
    
    # Including the global variables for total game wins 
    global totalAWins
    global totalBWins
    global totalCWins

    # Coin tossing and counting the heads and tails for each game
    while (coins > 0):
        flip1 = randint(0, 1)
        flip2 = randint(0, 1)

        # 1 means head
        if(flip1 == 1) and (flip2 == 1):
            groupAWins += 1
            coins -= 1

        # 0 means tails
        elif(flip1 == 0) and (flip2 == 0):
            groupBWins += 1
            coins -= 1

        # This is basically for prof group
        # A mixture of heads and tails
        elif(flip1 == 0) and (flip2 == 1) or (flip1 == 1) and (flip2 == 0):
            groupCWins += 1
            coins -= 1
            
    # Getting the percentages for each group in each game
    groupAPer = 0
    float(groupAPer)
    groupAPer = (((groupAWins * 1.0) / (groupAWins + groupBWins + groupCWins))) * 100.0
    groupBPer = 0
    float(groupBPer)
    groupBPer = (((groupBWins * 1.0) / (groupAWins + groupBWins + groupCWins))) * 100.0
    groupCPer = 0
    float(groupCPer)
    groupCPer = (((groupCWins * 1.0) / (groupAWins + groupBWins + groupCWins))) * 100.0

    # printing the output for each group in each game
    print ("Group A:   {}  ({}%);  Group B:    {}  ({}%);  Prof:  {}  ({}%)".format(groupAWins, groupAPer, groupBWins, \
                                                                                    groupBPer, groupCWins, groupCPer))

    # Adding points to the total of each group based on the percentage they get in each game
    if((groupCPer == groupBPer) and (groupCPer  > groupAPer)):
        win = randint (0, 1)
        if(win == 0):
            totalCWins += 1
        if(win == 1):
            totalBWins += 1
    if((groupAPer == groupBPer) and (groupAPer > groupCPer)):
        win = randint(0,1)
        if(win == 0):
            totalAWins += 1
        if(win == 1):
            totalBWins += 1
    if((groupAPer == groupBPer) and (groupAPer > groupBPer)):
        win = randint(0, 1)
        if (win == 0):
            totalAWins += 1
        if(win == 1):
            totalCWins += 1
    if((groupCPer == groupBPer) and (groupCPer > groupAPer)):
        win = randint(0, 1)
        if(win == 0):
            totalCWins += 1
        if(win == 1):
            totalBWins += 1
    elif (groupAPer > groupBPer) and (groupAPer > groupCPer):
        totalAWins += 1
    elif (groupBPer > groupAPer) and (groupBPer > groupCPer):
        totalBWins += 1
    elif (groupCPer > groupBPer) and (groupCPer > groupAPer):
        totalCWins += 1

# Printing the correct game number    
while (games > 0):
    print ("Games {}:".format(x))
    coinToss(coins)
    games -= 1
    x += 1

# Getting the percentages for the total game wins 
float(totalAPer)
totalAPer = (((totalAWins * 1.0) / (totalAWins + totalBWins + totalCWins))) * 100.0
float(totalBPer)
totalBPer = (((totalBWins * 1.0) / (totalAWins + totalBWins + totalCWins))) * 100.0
float(totalCPer)
totalCPer = (((totalCWins * 1.0) / (totalAWins + totalBWins + totalCWins))) * 100.0

# Printing the last line in the program which outputs the total game wins
print ("Group A:   {}  ({}%);  Group B:    {}  ({}%);  Prof:  {}  ({}%)".format(totalAWins, totalAPer, totalBWins, totalBPer, totalCWins, totalCPer))
