"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message"""


numb = (int(input("Enter a number to reveal if it is even or odd and if it's a multiple of 4: ")))
#  If you divide the input num by 2 and there remainder (mod - %) is 0 print even - else print odd
if numb % 2 == 0:
    print("even")
else:
    print ("odd")
#checks if number is a multiple of 4
if numb % 4 == 0:
    print("and is a multiple of 4")

print("-----------Check to see if a number divides into another number equally-------------")

num = (int(input("Enter a number: ")))
check = (int(input("Enter a number: " )))

if num % check == 0:
    print (check, "Divides evenly into" ,num)
else:
    print(check, "Does not Divide evenly into", num)