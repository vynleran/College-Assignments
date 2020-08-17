###########################################################################################
# Name: Parsa Jahanlou
# Date: Due April 24th, 2020
# Description: Program 4 --- 99 Bottles of Beer on the Wall
###########################################################################################

# the algorithm implemented recursively

def passsomebeer(beer):
    if (beer >= 2):
        print ("{} bottles of beer on the wall.".format(beer))
        print ("{} bottles of beer.".format(beer))
        print ("Take one down, pass it around")
        print ("{} {} of beer on the wall.".format(str(beer - 1), "bottle" if beer == 2 else "bottles"))
        print
        passsomebeer(beer - 1)
    elif (beer == 1):
        print ("{} bottle of beer on the wall.".format(beer))
        print ("{} bottle of beer.".format(beer))
        print ("Take one down, pass it around")
        print ("{} bottles of beer on the wall.".format(str(beer - 1)))
        print
        
###############################################
# MAIN PART OF THE PROGRAM
###############################################

passsomebeer(99)

