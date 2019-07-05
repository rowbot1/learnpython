"""
https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
"""
word = input("Enter Word to test if it is a palindrome: ")

#start at all of the word ':', stop at all of the word ':'
#https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python
# the -1 translates to lent(word)-1
letter = word[::-1] 

if word == letter:
    print("{} is a palindrome".format(word))
else:
    print("{} is NOT a palindrome".format(word))