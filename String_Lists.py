"""
https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
"""
word = input("Enter Word to test if it is a Palindrome: ")

#start at all of the word ':', stop at all of the word ':', step through it one letter at a time backwards '-1'
#https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python
# the -1 translates to lent(word)-1
letter = word[::-1] 

if word == letter:
    print("This is a Palindrome")
else:
    print("This is NOT a Palindrome")



