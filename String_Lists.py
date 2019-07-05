"""
https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
"""
word = input("Enter Word to test if it is a Palindrome: ")

letter = word[::-1] 
# print(letter, end= ' ' )  

if word == letter:
    print("This is a Palindrome")
else:
    print("This is NOT a Palindrome")



