import datetime

name = input("Enter Name: ")

age = int(input("Enter Age: "))

prediction = int(input(f"{name} enter age to see when you will be that old: "))

year = datetime.datetime.today().year

answer = year - age + prediction

one_hundred = year - age + 100

msg = f"{name} you will be {prediction} in the year {answer} and 100 in {one_hundred}"

print(msg)
