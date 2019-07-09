odd_even = int(input("Enter Number: "))

if odd_even % 2 == 0:
    print ("Number is Even")
else:
    print ("Number is Odd")
    
if odd_even % 4 == 0:
    print(f"{odd_even} is also a multiple of 4")
    
num = int(input("Enter 1 number: "))
check = int(input("Enter 2 number: "))

if num % check == 0:
    print (f"{check} divides into {num} evenly")
else:
    print(f"{check} does not divide into {num} evenly")
