###########################
# Name: Parsa Jahanlou
# Date: April 2nd, 2020
# Description: Python program 1
###########################
#Prompt the user for a first name, last name, age
first_name = input ("Please enter your first name: ")
#Basically, with the first_name variable, we are asking the user to enter their name and by making it a variable, we are using that for later.
last_name = input ("Please enter your last name: ")
#last_name variable asks for their last name which we are going to use later.
age = input ("How old are you, {} {}? ".format(first_name, last_name))
#age variable is meant for their age which will we used to calculate twice and half of their age
#Display the outputs below
print ("Hi {}. You are {} years old.".format(first_name, age))
print "Twice your age is " + str(age*2) + "."
print "Half your age is " + str(age/2.0) + "."
# Important explanation: In the rubric, it was mentioned that we must have good coding style. I did not know, which code you would prefer so i decided to include both of them.
###########################
# Name: Parsa Jahanlou
# Date: April 2nd, 2020
# Description: Python program 1
###########################
#Prompt the user for a first name, last name, age
first_name = input ("Please enter your first name: ")
#Basically, with the first_name variable, we are asking the user to enter their name and by making it a variable, we are using that for later.
last_name = input ("Please enter your last name: ")
#last_name variable asks for their last name which we are going to use later.
age = input ("How old are you, " + first_name + " " + last_name + "?")
#age variable is meant for their age which will we used to calculate twice and half of their age
#Display the outputs below
print "Hi " + first_name + ". You are " + str(age) + " " + "years old."
print "Twice your age is " + str(age*2) + "."
print "Half your age is " + str(age/2.0) + "."

