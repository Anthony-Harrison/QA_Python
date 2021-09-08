# Python is a high-level, interpreted and dynamically-typed programming 
# language that is very common in the technology industry.

# A programming language that is high level is designed to be simple for humans
# to understand.
# Where low level languages are harder to understand as the instructions are 
# closer to what a machine could understand.

# -----------------------------------------------------------------------------

# IDEs and Text editors
# These offer a tailored enviroment for programming from auto completing
# blocks of code, to colouring specific types of variable and objects.
# There are no 'best' IDEs or Text editors it is a case of what works best 
# for yourself. 
# Some examples of this include VSCode, Pycharm, and Eclipse. 

# -----------------------------------------------------------------------------

# Comments
# Comments are lines within Python that start with a # symbol and are ignored
# by the interpreter when a file is ran. By putting a # at the start of a line
# you can stop a line from being ran, such as a print statment. 
# This may be useful for when you want to avoid running something such as a 
# print statment without deleting the entire line.

# -----------------------------------------------------------------------------

# Variables 
# Variables are used to assign references to objects using a single =
# these can be used to store any of the 4 main data types.

# -----------------------------------------------------------------------------

# Data types 
# These are not explicitly stated when typing in the Python programming language
# instead they are interpreted as the lines of code are ran.
# There are 4 main data types in Python, these are.

# -----------------------------------------------------------------------------

# String - String objects must be within either " " or ' '
nameString = "Steve"
numberString = "123"

# Integer - A whole number
wholeNumberInteger = 456

# Floats - A decimal number
decimalNumberInteger = 6.78

# Booleans - A True or False statment
falseBoolean = False
trueBoolean = True

# -----------------------------------------------------------------------------

# Key Built-in Functions
# Python includes many built-in functions for us to use without 
# any imports required:

# print() - Displays data to the standard output, generally the terminal or cli.
print("Hello World") # Displays the string Hello World: Note the " " marks are 
#not in the output

# You can also print assigned variables.
print("Assigned variable printout", nameString)

# input() - Allows input from the standard input.
nameInput = input("Please enter your name. ")
# An input taken is always a String unless stated otherwise.
integerInput = int(input("Please enter your age. "))

# type() - Gives the data-type of an attribute of data.
print("Type of variable numberString is. ", type(numberString))
print("Type of variable wholeNumber integer is. ", type(wholeNumberInteger))

# -----------------------------------------------------------------------------

# Syntax
# How a statment is typed matters when programming. Spelling and punctuation
# mistakes will stop a program from running correctly.

# Uncomment these lines below.
#Print("Hello World") # Will not run because the 'P' in print is capitalised.
#print("Hello World" # Will not run because a closing bracket is missing.

# -----------------------------------------------------------------------------

#Basic mathematics can be performed in Python:

#Addition - '+'
#Subtraction - '-'
#True Division - '/'
#Floor Division - '//'
#Multiplication - '*'
#Powers - '**'
#Modulus - '%'

#Python will execute mathematics using BIDMAS:
#
#B - Brackets - ( )
#I - Indices - **
#D - Division - / or //
#M - Multiplication - *
#A - Addition - +
#S - Subtraction - -