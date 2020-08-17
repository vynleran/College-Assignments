#######################################
# Name: Parsa Jahanlou
# Date: April 9th, 2020
# Description: Python Program 2 (Easy Does It.... Reloaded)
#######################################

def first_name():
    return input ("Please enter your first name: ")
# Function that prompts the user for a first name and returns it
def last_name():
    return input ("Please enter your last name: ")
# Function that prompts the user for a last name and returns it
def age(users_fn, users_ln):
    return input ("How old are you, {} {}? ".format(users_fn, users_ln))
# Function that prompts the user for their age and returns it
def greet(users_fn, users_ln, users_age):
    print ("Hi {} {}. You are {} years old.".format(users_fn, users_ln, users_age))
    print "Twice your age is " + str(users_age*2) + "."
    print "Half your age is " + str(users_age/2.0) + "."
# Function takes the first name, the last name, and the age as parameters and prints outputs.
'''
users_fn = first_name()
users_ln = last_name()
users_age = age(users_fn, users_ln)
'''
#######################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
#######################################

users_fn = first_name()
# getting the user's first name
users_ln = last_name()
# getting the user's last name
users_age = age(users_fn, users_ln)
# geeting the user's age
greet(users_fn, users_ln, users_age)
#greeting the user




