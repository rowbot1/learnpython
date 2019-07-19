"""
https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes."""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(b)
print("\nNumbers that are both in list a and b: ")
for num in a:
    if num in b:
        print(num, end=" ")

import random

num1 = int(input("\nSize of List in List 1: "))
num2 = int(input("Size of List 2: "))

list1 = range(num1)
list2 = range(num2)


first_list = random.sample(list1, k=10)
print("First List: ", first_list)
second_list = random.sample(list2, k=10)
print("Second List: ", second_list)

print("Similar Numbers")

for numb in first_list:
    if numb in second_list:
        print(numb, end=" ")
