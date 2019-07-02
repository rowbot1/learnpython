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