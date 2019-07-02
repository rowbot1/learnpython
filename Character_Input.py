"""
https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""


name = input("What is your name:  ")
#make input an integer 
age = (int(input("Enter you age:  ")))

import datetime
#get date and time now
now = datetime.datetime.now()

#extract year only and subtract the input age and add 100
calc = int(now.strftime("%Y")) - age + 100

msg = "hello" , name , "you are" , age , "and you will be one hundred in the year", calc
print (msg)

"""Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Taking input """

another_number = (int(input("How many times do you want to see the previous message? ")))
x = 1
while x is not another_number + 1:
    print (msg)
    x = x + 1
